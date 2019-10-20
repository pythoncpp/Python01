from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    print("inside root")
    return "this is the home page"


app.run(host="0.0.0.0", port=4000)
