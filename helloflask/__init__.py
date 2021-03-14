from flask import Flask
from flask import g
app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
    print("br")
    g.str="한글"

@app.route("/")
def helloworld():
    return "Hello Flask World" + getattr(g, 'str', '111')


