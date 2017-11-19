from flask import Flask
from flask import render_template
from flask import jsonify
from twitter.tweetcontainer import TweetContainer
import json

app = Flask(__name__)

@app.route('/')

def init():
    return render_template('index.html')
   #return 'Hello, is it me you\'re looking for?'

@app.route('/ipost/<username>')
def get_igram_posts(username):
    # Get the instagram posts of the user
    return 'Username %s' % username

@app.route('/tpost/<username>/<count>')
def show_tweets(username, count):
    tweetContainer = TweetContainer(username)
    tweetContainer.load(20)
    return jsonify(tweetContainer.toDict(int(count)))
