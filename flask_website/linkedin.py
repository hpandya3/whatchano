import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json


#Import API Key and Search Engine ID
config = json.load(open('.\config.json'))

def getGoogleSearch(name):
    try:
        search_string = name.replace(" ", "+")
        url = "https://www.googleapis.com/customsearch/v1?key=" + config["googleapi_key"] + "cx=" + config["custom_searchengine_id"] + "&q=" + search_string
        r = requests.get('')