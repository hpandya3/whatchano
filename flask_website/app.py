from flask import Flask
from flask import render_template
from flask import jsonify

from twitter.tweetcontainer import TweetContainer
from flask import Response
from instagram import get_worst_posts

app = Flask(__name__)

@app.route('/')

def init():
    return render_template('index.html')
   #return 'Hello, is it me you\'re looking for?'

@app.route('/ipost/<username>')
def get_igram_posts(username):
    result = get_worst_posts(username, 'username', 3)
    return Response(result, mimetype='application/json')

@app.route('/tpost/<username>/<count>')
def show_tweets(username, count):
    tweetContainer = TweetContainer(username)
    tweetContainer.load(100)
    return jsonify(tweetContainer.toDict(int(count)))

@app.route('/ipost/tag/<tag>')
def get_igram_posts_from_tag(tag):
    # Get the instagram posts of the user
    result = get_worst_posts(tag, 'tag', 3)
    return Response(result, mimetype='application/json')
