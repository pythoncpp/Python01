from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def function1():
    # load the chrome web driver
    chrome = webdriver.Chrome()

    # navigate to the url
    chrome.get("https://google.co.in")

    # find the input with name = q
    input = chrome.find_element_by_name('q')

    # search for iphone 11 pro
    input.send_keys('iphone 11 pro')

    # press enter
    input.send_keys(Keys.ENTER)

    # close the browser
    chrome.close()


# function1()


def function2():
    chrome = webdriver.Chrome()
    chrome.get("file:///Volumes/Data/Sunbeam/2019/August/workshops/Python01/day_16/client/login.html")

    # find user name input
    input_username = chrome.find_element_by_id('username')
    input_username.send_keys('amitk')
    time.sleep(2)

    # find password input
    input_password = chrome.find_element_by_id('password')
    input_password.send_keys('test')
    time.sleep(2)

    # find the button
    button = chrome.find_element_by_id('login')
    button.click()

    time.sleep(2)

    chrome.close()


# function2()


def function3():
    chrome = webdriver.Chrome()
    chrome.get("https://weather.com/en-IN/weather/tenday/l/Pune+Maharashtra?canonicalCityId=c9591c73a867f5d9f013e7ad7bcc02e7dcdfe28e3166c52b0177a2b5405c6238")

    time.sleep(1)

    # find table
    table = chrome.find_element_by_class_name('twc-table')

    # find tbody
    tbody = table.find_element_by_tag_name('tbody')

    # find list of tr
    rows = tbody.find_elements_by_tag_name('tr')

    # used to collect the weather data
    data = []

    # open the csv file
    temp_csv = open('temp.csv', 'w')

    # title row
    temp_csv.write('day,description,high,low\n')

    for row in rows:

        # find td elements
        columns = row.find_elements_by_tag_name('td')

        # for column in columns:
        #     # print(column.text)

        # find day
        span = columns[1].find_element_by_class_name('day-detail')
        day = span.text

        # find description
        description = columns[2].find_element_by_tag_name('span').text

        # find the temperature values
        temp_spans = columns[3].find_elements_by_tag_name('span')
        high = temp_spans[0].text.replace('°', '')
        low = temp_spans[2].text.replace('°', '')

        d = {
            "day": day,
            "description": description,
            "high": high,
            "low": low
        }

        data.append(d)

        # write the data line by line
        temp_csv.write(f"{day},{description},{high},{low}\n")

    time.sleep(1)

    print(data)

    # save the data into json format
    # temp_json = open('temp.json', 'w')
    # temp_json.write(str(data))
    # temp_json.close()

    chrome.close()

    # close csv file
    temp_csv.close()


function3()


