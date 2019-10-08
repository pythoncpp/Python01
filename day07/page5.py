# 2, 4, 6, 8, 10..
# 3, 9, 12...


def function1():
    numbers = list(range(1, 11))
    print(list(map(lambda x: x * 2, numbers)))
    print(list(map(lambda x: x * 3, numbers)))


# function1()


def number_table(num):
    def inner_number_table(count=10):
        numbers = list(range(1, count + 1))
        print(list(map(lambda x: x * num, numbers)))

    return inner_number_table


# table_2 = number_table(2)
# table_2(100)


# <h1>header1</h1>
# <h1>header2</h1>
# <h1>header3</h1>
# <h2>header1</h2>
# <h2>header2</h2>
# <div>div1</div>
# <div>div2</div>
# <div>div3</div>
# <p>p1</p>
# <p>p2</p>
# <p>p3</p>


# print("<h1>header1</h1>")

def html_output(tag, data):

    def header1(data):
        print("<h1>", data, "<h1>")

    def header2(data):
        print("<h2>", data, "<h2>")

    def header3(data):
        print("<h3>", data, "<h3>")

    def div(data):
        print("<div>", data, "<div>")

    def p(data):
        print("<p>", data, "<p>")

    if tag == "h1":
        header1(data)
    elif tag == "h2":
        header2(data)
    elif tag == "h3":
        header3(data)
    elif tag == "div":
        div(data)
    elif tag == "p":
        p(data)


# html_output('h1', 'header1')
# html_output('h2', 'header2')
# html_output('div', 'div1')
# html_output('p', 'p1')


def html_output_1(tag, data):
    def inner_function1():
        print("<", tag, ">", data , "</", tag, ">")

    return inner_function1


# function = html_output_1('h1', 'header1')
# function()
#
# function2 = html_output_1('h1', 'header 1 1')
# function2()


def html_output_3(tag):
    def inner_function(data):
        print("<", tag, ">", data, "</", tag, ">")

    return inner_function


h1 = html_output_3('h1')
h1('header1')
h1('header 111')
h1('header 1111')

div = html_output_3('div')
div('div1')
div('div2')
div('div3')
























