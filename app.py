from flask import Flask

from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def root():
    return "Service 2"

@app.route("/hello/<username>")
def hello(username):
    return "Hello {} from Service 2".format(
        escape(username)
    )
