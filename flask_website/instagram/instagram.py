import requests
import json
import re
from operator import itemgetter
from preprocessing.preprocessing import preprocess
from sentiment_analysis.sentiment import getSentiment

def get_cursor(raw_data, method):
    
    if method == 'username':
        page_info = raw_data['user']['media']['page_info']
    elif method == 'tag':
        page_info = raw_data['tag']['media']['page_info']

    has_next_page = page_info['has_next_page']

    if has_next_page == True:
        cursor = page_info['end_cursor']

        return cursor

    return None


def get_posts(method, url, raw):

    if method == 'username':
        nodes = raw['user']['media']['nodes']

    elif method == 'tag':
        nodes = raw['tag']['media']['nodes']

    cursor = get_cursor(raw, method)

    if cursor is not None:

        """
        The end argument is to set a limit to the number of pages to crawl. If
        placed to 0 it will be all pages.
        """
        posts = crawl_pages(nodes, url, method, cursor, 20)

    else:
        posts = nodes

    return posts


def crawl_pages(result, url, method, cursor, limit=0, count=0):

    next_page_url = url + "&max_id=" + cursor

    fetch_additional = requests.get(next_page_url).json()

    if method == 'username':
        new_nodes = fetch_additional['user']['media']['nodes']
    elif method == 'tag':
        new_nodes = fetch_additional['tag']['media']['nodes']

    append_results = result + new_nodes

    next_cursor = get_cursor(fetch_additional, method)

    if next_cursor is not None:

        if limit == 0:
            return crawl_pages(append_results, url, method, next_cursor)

        elif count < limit:
            count = count + 1
            return crawl_pages(append_results, url, method, next_cursor, limit, count)

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


def get_instagram_results(query, method):

    if method == 'username':
        url = "https://www.instagram.com/" + query +"/?__a=1"

    elif method == 'tag':
        url = "https://www.instagram.com/explore/tags/" + query + "/?__a=1"
    
    else:
        return 0

    fetch_data = requests.get(url)
    feed = fetch_data.json()

    posts = get_posts(method, url, feed)
    append_hashtags = store_in_hashtags(posts)

    final_out = dict()
    final_out['posts'] = append_hashtags

    if method == 'username':
        name = feed['user']['full_name']
        final_out['full_name'] = name

    elif method == 'tag':
        name = feed['tag']['name']
        final_out['name'] = name

    return final_out


def get_worst_posts(query, method, num_of_posts):

    insta_results = get_instagram_results(query, method)

    posts = insta_results['posts']

    def map_sentiment_value(post):
        if 'caption' in post:
            caption = post['caption']
            preprocessed_text = preprocess(caption)
            result = getSentiment(preprocessed_text)
            post['sentiment'] = result
            post['sentiment_neg'] = result['compound']
        else:
            post['sentiment'] = ""
            post['sentiment_neg'] = 0

        return post

    sentiment_posts = list(map(map_sentiment_value, posts))

    worst_sentiment_sorted = sorted(
        sentiment_posts,
        key=itemgetter('sentiment_neg'),
        reverse=False)

    insta_results['posts'] = worst_sentiment_sorted[:num_of_posts]

    return json.dumps(insta_results)
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
