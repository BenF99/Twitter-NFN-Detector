#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# =============================================================================
"""Using Fine-Tuned XLNet model for classification"""
# =============================================================================
# Imports
from simpletransformers.classification import ClassificationModel, ClassificationArgs
from scipy.special import softmax
from transformers import XLNetTokenizer, DebertaTokenizer, logging
# =============================================================================
# Hide Language Model Outputs
logging.set_verbosity_error()
# =============================================================================


class XLNetDeBERTaClassification:

    def __init__(self, model, model_dir="D:/Language Models/"):
        model_pn = {'xlnet': f'{model_dir}{"XLNET-LARGE/"}',
                    'deberta': f'{model_dir}{"DEBERTA-LARGE/"}'
                    }[model]
        self.model = ClassificationModel(model, model_pn, use_cuda=False)
        self.tokenizer = XLNetTokenizer.from_pretrained(model_pn) if model == 'xlnet' \
            else DebertaTokenizer.from_pretrained(model_pn)
        self._text = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, raw_text):
        if not isinstance(raw_text, str):
            raise TypeError("Error: Invalid Input Type")
        else:
            self._text = raw_text

    def check_probs(self):
        _, logits = self.model.predict([self._text])
        probs = softmax(logits[0])
        probs_3dp = ["{:.5f}".format(float(i)) for i in probs]
        return probs_3dp, len(self.tokenizer.encode(self._text, add_special_tokens=False))
