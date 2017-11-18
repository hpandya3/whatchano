from flask import Flask

app = Flask(__name__)

@app.route('/')

def init():
    return 'Hello, is it me you\'re looking for?'