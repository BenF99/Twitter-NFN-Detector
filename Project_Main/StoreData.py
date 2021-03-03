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

    def __init__(self, text, hashtag, fake, real, token_count, url, model):
        self.text, self.hashtag, self.fake, self.real, self.token_count, self.url, self.model = text, hashtag, fake, \
                                                                                                real, token_count, url,\
                                                                                                model
        self.ref = db.reference("Twitter NFN Detector")
        self.child_node = 'real' if self.fake < self.real else 'fake'

    # TODO: If data exists, return probabilities

    def exists(self):
        node_dict = self.ref.child(self.child_node).get()
        for v in node_dict.values():
            if self.text == v['text'] and self.model == v['model']:
                return True
        return False

    def store(self):
        if not self.exists():
            id_ref = self.ref.child(self.child_node).push()
            id_ref.set({
                'text': self.text,
                'hashtag': self.hashtag,
                'fake': self.fake,
                'real': self.real,
                'token_count': self.token_count,
                'url' : self.url,
                'model' : self.model

            })
