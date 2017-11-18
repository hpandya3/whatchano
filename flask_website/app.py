from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def init():
    return render_template('index.html')
   #return 'Hello, is it me you\'re looking for?'