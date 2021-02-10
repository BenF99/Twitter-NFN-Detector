#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# Date Last Updated : 09/02/2021 - 15:43
# =============================================================================
"""Main wrapper for classes"""
# =============================================================================
# Imports
import configparser
import time

import firebase_admin
from firebase_admin import credentials
from SequenceClassification import SequenceClassification
from StoreData import StoreData
from tweetGetter import TweetGetter
import anvil.server
# =============================================================================
# Setup Credentials and Server Connection
config = configparser.ConfigParser()
config.read("C:/Users/User/Desktop/Project_Main/apikeys.ini")
#anvil.server.connect(config['server']['key'])

cred = credentials.Certificate("C:/Users/User/Desktop/Project_Main/twitter-nfn-detector-firebase.json")
app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://twitter-nfn-detector-default-rtdb.europe-west1.firebasedatabase.app/'
})
# =============================================================================


def getprobs(text):
    sq = SequenceClassification()
    sq.text = text
    probs, num_tokens = sq.check_probs()
    fake, real = probs[0], probs[1]
    print('fake' if fake > real else 'real')
    return fake, real, num_tokens


#@anvil.server.callable
def getprobscustom(text):
    fin_url = "N/A"
    if "twitter.com/" in text.lower():
        t = TweetGetter()
        t.tweet = text.split('/')[-1].split('?')[0]
        text, tweet_content, fin_url = t.gettweetdata(t.tweet)[0:2]
        text = tweet_content if tweet_content else text
    fake, real, num_tokens = getprobs(text)
    StoreData(text, "N/A", fake, real, num_tokens, fin_url).store()
    return fake, real


#@anvil.server.callable
def getprobstweet(hashtag):
    t = TweetGetter()
    tweet, ht = t.getrecentweet(hashtag)
    t.tweet = tweet
    tweet, tweet_content, fin_url = t.gettweetdata(t.tweet)
    text = tweet_content if tweet_content else tweet
    fake, real, num_tokens = getprobs(text)
    StoreData(tweet, ht, fake, real, num_tokens, fin_url).store()

    return tweet, fake, real, fin_url


#anvil.server.wait_forever()

for i in range(1,500):
    getprobstweet(None)
    time.sleep(5)