import urllib, json
from selenium import webdriver
import time

def look_for_new_video():
    api_key = "get your api key: https://console.developers.google.com"
    channel_id = "paste your channel id here"
    
    base_video_url = "https://www.youtube.com/watch?v="
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"
    