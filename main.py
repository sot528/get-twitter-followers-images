#!/usr/bin/env python
# -*- coding:utf-8 -*-

# noinspection PyUnresolvedReferences
from time import sleep

# noinspection PyUnresolvedReferences
import tweepy

CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
ACCESS_TOKEN = 'xxx'
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

for user in tweepy.Cursor(api.followers, screen_name="ALIS_media", count=200).items():
    with open('follower_image_urls.txt', 'a') as f:
        f.write(user.profile_image_url + '\n')

    # For API rate limit
    sleep(0.4)
