#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# =============================================================================
"""Main wrapper for classes"""
# =============================================================================
# Imports
import configparser
import random
import time

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


def store(sd, ht, f, r, nt, fu):
    sd.hashtag = ht
    sd.fake = f
    sd.child_node = 'fake' if f > r else 'real'
    sd.real = r
    sd.token_count = nt
    sd.url = fu
    sd.store()


@anvil.server.callable
def response(text, model, is_hashtag=True):
    model = model.lower()
    t = TweetGetter()
    tweet = None
    if is_hashtag:
        tweet, ht = t.getrecentweet(text)
        t.tweet = tweet
        tweet, text, fin_url = t.gettweetdata(t.tweet)
    else:
        ht = "N/A"
        fin_url = "N/A"
        if "twitter.com/" in text.lower():
            t.tweet = text.split('/')[-1].split('?')[0]
            tweet, text, fin_url = t.gettweetdata(t.tweet)
    sd = StoreData(text, model)
    e_ = sd.exists()
    if e_:
        fake, real = e_
    else:
        fake, real, num_tokens = getprobs(text, model)
        store(sd, ht, fake, real, num_tokens, fin_url)
    if is_hashtag:
        return tweet, fake, real, fin_url
    else:
        return fake, real

anvil.server.wait_forever()

# "Further investigation"
# models = ["roberta", "deberta", "xlnet"]
# for i in range(0,500):
#     time.sleep(8)
#     response(None, random.choice(models))
