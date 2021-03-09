#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# Date Last Updated : 09/02/2021 - 15:43
# =============================================================================
"""Database Component - Add/Retrieve"""
# =============================================================================
# Imports
from firebase_admin import db


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
            'model': self.model

        })
