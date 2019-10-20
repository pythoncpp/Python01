from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

# enable the CORS
CORS(app)


@app.route('/')
def root():
    return "<h1>this is my home page</h1>"


@app.route('/user', methods=["GET"])
def get_users():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute('select * from User')

    # list of tuples
    result = cursor.fetchall()

    users = []
    for (id, name, username, password, email, address) in result:
        # converted the tuple into a dictionary
        user = {
            "id": id,
            "name": name,
            "username": username,
            "email": email,
            "address": address
        }

        users.append(user)

    cursor.close()
    db.close()

    # convert the data into json structure
    return jsonify(users)


@app.route('/user/login', methods=["POST"])
def login_user():
    user = request.json.get('username')
    password = request.json.get('password')

    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute(f"select * from User where username = '{user}' and password = '{password}';")
    result = cursor.fetchall()

    is_successfull_login = False
    if len(result) == 0:
        is_successfull_login = False
        print("wrong user name or password")
    else:
        is_successfull_login = True
        print("welcome to my application")

    cursor.close()
    db.close()

    response = {"status": is_successfull_login}
    return response


@app.route('/user/register', methods=["POST"])
def register_user():
    full_name = request.json.get('full_name')
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    address = request.json.get('address')

    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute(f"insert into User (full_name, username, password, email, address) values ('{full_name}', '{username}', '{password}', '{email}', '{address}')")
    db.commit()
    cursor.close()
    db.close()

    return "registered"


@app.route('/product', methods=["GET"])
def get_products():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute('select * from Product')
    result = cursor.fetchall()
    products = []
    for (id, title, price, description) in result:
        products.append({
            "id": id, "price": price, "description": description, "title": title
        })

    cursor.close()
    db.close()
    return jsonify(products)


@app.route('/product', methods=["POST"])
def insert_product():
    print("inside insert production function")
    # print(request.json)

    title = request.json.get('title')
    description = request.json.get('description')
    price = request.json.get('price')

    db = mysql.connector.connect(host="localhost", user="root", password="root", database="final_app_db")
    cursor = db.cursor()
    cursor.execute(f"insert into Product (title, price, description) values ('{title}', {price}, '{description}')")
    db.commit()
    cursor.close()
    db.close()
    print('new record is now inserted..')
    return "inserted.."



app.run(host="0.0.0.0", port="4000")
