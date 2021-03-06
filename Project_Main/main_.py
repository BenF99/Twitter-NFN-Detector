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
import firebase_admin
from firebase_admin import credentials

from roberta import RoBERTaClassification
from xlnetdeberta import XLNetDeBERTaClassification
from StoreData import StoreData
from tweetGetter import TweetGetter
import anvil.server

# =============================================================================
# Setup Credentials and Server Connection
config = configparser.ConfigParser()
config.read("C:/Users/User/Desktop/Project_Main/apikeys.ini")
anvil.server.connect(config['server']['key'])

cred = credentials.Certificate("C:/Users/User/Desktop/Project_Main/twitter-nfn-detector-firebase.json")
app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://twitter-nfn-detector-default-rtdb.europe-west1.firebasedatabase.app/'
})
# =============================================================================


def getprobs(text, model):
    if model == "roberta":
        sq = RoBERTaClassification()
    else:
        sq = XLNetDeBERTaClassification(model)
    sq.text = text
    probs, num_tokens = sq.check_probs()
    fake, real = probs[0], probs[1]
    print('fake' if fake > real else 'real')
    return fake, real, num_tokens


@anvil.server.callable
def response(text, model, is_hashtag=True):
    t = TweetGetter()
    tweet = None
    if is_hashtag:
        tweet, ht = t.getrecentweet(text)
        t.tweet = tweet
        tweet, tweet_content, fin_url = t.gettweetdata(t.tweet)
        text = tweet_content if tweet_content else tweet
    else:
        ht = "N/A"
        fin_url = "N/A"
        if "twitter.com/" in text.lower():
            t.tweet = text.split('/')[-1].split('?')[0]
            tweet, tweet_content, fin_url = t.gettweetdata(t.tweet)
            text = tweet_content if tweet_content else tweet

    fake, real, num_tokens = getprobs(text, model.lower())
    StoreData(text, ht, fake, real, num_tokens, fin_url, model).store()
    if is_hashtag:
        return tweet, fake, real, fin_url
    else:
        return fake, real


anvil.server.wait_forever()
