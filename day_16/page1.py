import mysql.connector


def function1():
    # connect the application to mysql db
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")

    # create cursor
    cursor = db.cursor()

    # insert operation
    cursor.execute("insert into User (full_name, username, password, email, address) values ('bill gates', 'bill', 'bill', 'bill@ms.com', 'usa')")

    # commit operation
    db.commit()

    # close the cursor
    cursor.close()

    # close the db
    db.close()

    print('new record is now inserted..')


# function1()


def function2():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute('select * from User')

    # get all the rows
    # list of tuples
    users = cursor.fetchall()

    # print(result)

    # for user in users:
    #     print(f"id:{user[0]}, name:{user[1]}, username:{user[2]}, password:{user[3]}, address:{user[4]}")

    for (id, name, username, password, email, address) in users:
        print(f"id: {id}, name: {name}, username: {username}, password: {password}, email: {email}, address: {address}")

    cursor.close()
    db.close()


# function2()


def function3():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute("update User set address = 'india' where id = 3")
    cursor.close()
    db.commit()
    db.close()


# function3()


def function4():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute("delete from User where id = 3")
    cursor.close()
    db.commit()
    db.close()


# function4()


def function5():
    # check if user can login
    print("enter user name:")
    user = input()

    print("enter password:")
    password = input()

    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute(f"select * from User where username = '{user}' and password = '{password}';")
    result = cursor.fetchall()

    if len(result) == 0:
        print("wrong user name or password")
    else:
        print("welcome to my application")

    cursor.close()
    db.close()


function5()
