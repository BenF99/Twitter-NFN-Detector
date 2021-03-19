#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# =============================================================================
"""Database Component - Add/Retrieve"""
# =============================================================================
# Imports
from firebase_admin import db
from datetime import datetime

# =============================================================================


class StoreData:

    def __init__(self, text, model):
        self.hashtag = self.fake = self.real = self.token_count = self.url = self.child_node = None
        self.text, self.model = text, model
        self.ref = db.reference("Twitter NFN Detector")

    def exists(self):
        fake_dict = self.ref.child('fake').get()
        real_dict = self.ref.child('real').get()
        for v in real_dict.values():
            if self.text == v['text'] and self.model == v['model']:
                return v['fake'], v['real']
        for v in fake_dict.values():
            if self.text == v['text'] and self.model == v['model']:
                return v['fake'], v['real']
        return False

    def store(self):
        id_ref = self.ref.child(self.child_node).push()
        id_ref.set({
            'text': self.text,
            'hashtag': self.hashtag,
            'fake': self.fake,
            'real': self.real,
            'token_count': self.token_count,
            'url': self.url,
            'model': self.model,
            'datetime': str(datetime.today().strftime('%d-%m-%Y %H:%M'))
        })

    # def count(self):
    #     fake_dict = self.ref.child('fake').get()
    #     real_dict = self.ref.child('real').get()
    #     print(len(fake_dict.keys()))
    #     print(len(real_dict.keys()))
    #
    # def avgtoken(self):
    #
    #     fake_dict = self.ref.child('fake').get()
    #     len_tc = len(fake_dict.keys())
    #     t = 0
    #     for v in fake_dict.values():
    #         t += v['token_count']
    #     print(t/len_tc)
