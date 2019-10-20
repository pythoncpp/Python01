from flask import Flask

# create a flask application
app = Flask(__name__)


# when the url is / and method is GET then call this method
@app.route('/')
def welcome():
    return "<h1>welcome to the application</h1>"


# execute the application
app.run()
