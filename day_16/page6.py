from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def graph():
    return send_file('age_vs_salary.png')


app.run()