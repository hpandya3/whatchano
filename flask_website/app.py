from flask import Flask
from flask import render_template
from flask import Response
from .instagram import get_worst_posts

app = Flask(__name__)

@app.route('/')

def init():
    return render_template('index.html')
   #return 'Hello, is it me you\'re looking for?'

@app.route('/ipost/<username>')
def get_igram_posts(username):
    # Get the instagram posts of the user
    result = get_worst_posts(username, 'username', 3)
    return Response(result, mimetype='application/json')

@app.route('/ipost/tag/<tag>')
def get_igram_posts_from_tag(tag):
    # Get the instagram posts of the user
    result = get_worst_posts(tag, 'tag', 3)
    return Response(result, mimetype='application/json')

@app.route('/tpost/<username>')
def show_post(username):
    # show the post with the given id, the id is an integer
    return 'Username %s' % username
