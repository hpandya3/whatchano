import requests
import json
import re
from operator import itemgetter
from preprocessing.preprocessing import preprocess
from sentiment_analysis.sentiment import getSentiment

def get_cursor(raw_data):
    
    page_info = raw_data['user']['media']['page_info']
    has_next_page = page_info['has_next_page']

    if has_next_page == True:
        cursor = page_info['end_cursor']

        return cursor

    return None


def get_posts(url, raw):

    cursor = get_cursor(raw)
    nodes = raw['user']['media']['nodes']

    if cursor is not None:

        """
        The end argument is to set a limit to the number of pages to crawl. If
        placed to 0 it will be all pages.
        """
        posts = crawl_pages(nodes, url, cursor, 6)

    return posts


def crawl_pages(result, url, cursor, limit=0, count=0):

    next_page_url = url + "&max_id=" + cursor

    fetch_additional = requests.get(next_page_url).json()
    new_nodes = fetch_additional['user']['media']['nodes']
    append_results = result + new_nodes

    next_cursor = get_cursor(fetch_additional)

    if next_cursor is not None:

        if limit == 0:
            return crawl_pages(append_results, url, next_cursor)

        elif count < limit:
            count = count + 1
            return crawl_pages(append_results, url, next_cursor, limit, count)

    return append_results


def store_in_hashtags(posts):

    def map_hashtags(post):
        if 'caption' in post:
            hashtags = re.findall(r"#(\w+)", post['caption'])
        else:
            hashtags = ""
        post['hashtags'] = hashtags
        return post

    updated_posts = list(map(map_hashtags, posts))

    return updated_posts


def get_instagram_results(username):

    url = "https://www.instagram.com/" + username +"/?__a=1"

    fetch_data = requests.get(url)
    feed = fetch_data.json()

    posts = get_posts(url, feed)

    full_name = feed['user']['full_name']

    append_hashtags = store_in_hashtags(posts)

    final_out = dict()
    final_out['full_name'] = full_name
    final_out['posts'] = append_hashtags

    return final_out


def get_worst_posts(username, num_of_posts):

    insta_results = get_instagram_results(username)

    posts = insta_results['posts']

    def map_sentiment_value(post):
        if 'caption' in post:
            caption = post['caption']
            preprocessed_text = preprocess(caption)
            result = getSentiment(preprocessed_text)
            post['sentiment'] = result
            post['sentiment_compound'] = result['neg']
        else:
            post['sentiment'] = ""
            post['sentiment_compound'] = 0

        return post

    sentiment_posts = map(map_sentiment_value, posts)

    worst_sentiment_sorted = sorted(
        sentiment_posts,
        key=itemgetter('sentiment_compound'),
        reverse=True)

    return json.dumps(worst_sentiment_sorted[:num_of_posts])
"""
    def filter_neg_compound(post):
        if post['sentiment_compound'] < 0:
            return post

    filter_negatives = list(
        filter(filter_neg_compound, worst_sentiment_sorted))

    # Because 'likes' is stored in a sub index called 'count' we'll map to get
    # it out :( I know it's dirty
    def map_likes(post):
        likes = post['likes']['count']
        post['likes'] = likes
        return post

    added_likes = list(map(map_likes, filter_negatives))

    least_liked_posts = sorted(added_likes, key=itemgetter('likes'), reverse=False)
"""
