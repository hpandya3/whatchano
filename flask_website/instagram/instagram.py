import requests
import json
import re

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

        posts = crawl_pages(nodes, url, cursor)

    return posts


def crawl_pages(result, url, cursor):

    next_page_url = url + "&max_id=" + cursor

    fetch_additional = requests.get(next_page_url).json()
    new_nodes = fetch_additional['user']['media']['nodes']
    append_results = result + new_nodes

    next_cursor = get_cursor(fetch_additional)

    if next_cursor is not None:
        return crawl_pages(append_results, url, next_cursor)

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

    return json.dumps(final_out)
