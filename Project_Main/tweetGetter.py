#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# Date Last Updated : 12/01/2021 - 17:15
# =============================================================================
"""Extracting and Refining tweets received by client"""
# =============================================================================
# Imports
import time
import trafilatura
from twitter import *
import configparser
# =============================================================================


class TweetGetter:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("apikeys.ini")
        self.token = config['twitter']['token']
        self.token_secret = config['twitter']['token_secret']
        self.consumer_key = config['twitter']['consumer_key']
        self.consumer_secret = config['twitter']['consumer_secret']
        self._tweet = None
        self.t = Twitter(
            auth=OAuth(self.token, self.token_secret, self.consumer_key, self.consumer_secret))
        self.tm = 'extended'

    @property
    def tweet(self):
        return self._tweet

    @tweet.setter
    def tweet(self, t_id):
        self._tweet = self.t.statuses.show(_id=t_id, tweet_mode=self.tm)

    def getrecentweet(self, hashtag):
        _hts = "#news"
        if hashtag:
            _hts = hashtag.split()
            _hts = ' '.join(['#' + x if x[0] != '#' else x for x in _hts])
            q = "{} -filter:retweets".format(_hts)
        else:
            q = "#news -filter:retweets"
        while True:
            tweet = self.t.search.tweets(q=q, tweet_mode=self.tm, count=2)
            if tweet['statuses'] == [] or tweet['statuses'][0]['lang'] != 'en':
                time.sleep(5)
            else:
                print("id:", tweet['statuses'][0]['id_str'])
                return tweet['statuses'][0]['id_str'], _hts

    @staticmethod
    def gettweetdata(tweet):
        full_tweet = tweet['full_text']
        if tweet['entities']['urls']:
            urls = []
            for i in range(len(tweet['entities']['urls'])):
                urls.append(tweet['entities']['urls'][i]['expanded_url'])
            final_text = extractcontents(urls)[0]
        else:
            final_text = full_tweet

        fin_url = "https://twitter.com/twitter/statuses/" + tweet['id_str']

        return full_tweet, final_text, fin_url


def extractcontents(urls):
    raw_contents = []
    for i in range(len(urls)):
        d = trafilatura.fetch_url(urls[i])
        raw_contents.append(trafilatura.extract(d, include_comments=False))
    return raw_contents
