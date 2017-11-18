from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def init():
    return render_template('index.html')


@app.route('/ipost/<username>')
def get_igram_posts(username):
    # Get the instagram posts of the user
    return 'Username %s' % username 

@app.route('/tpost/<username>')
def show_post(username):
    # show the post with the given id, the id is an integer
    return 'Username %s' % username