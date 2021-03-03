#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# Date Last Updated : 09/02/2021 - 15:42
# =============================================================================
"""Using Fine-Tuned XLNet model for classification"""
# =============================================================================
# Imports
from simpletransformers.classification import ClassificationModel, ClassificationArgs
from scipy.special import softmax
from transformers import XLNetTokenizer, logging

# =============================================================================
# Hide Language Model Outputs
logging.set_verbosity_error()
# =============================================================================

class XLNetClassification:

    def __init__(self, model_pn="D:/Language Models/XLNET-LARGE/"):
        self._text = None
        # Hyperparameters
        # model_args = ClassificationArgs(num_train_epochs=2,
        #                                 warmup_ratio=0.1,
        #                                 train_batch_size=12,
        #                                 labels_list=['machine', 'human'],
        #                                 overwrite_output_dir=True,
        #                                 learning_rate=2e-5,
        #                                 save_model_every_epoch=True,
        #                                 use_multiprocessing=False,
        #                                 save_steps=-1)
        self.model = ClassificationModel("xlnet", model_pn, use_cuda=False)
        self.tokenizer = XLNetTokenizer.from_pretrained(model_pn)

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
        probs_2dp = [("{:.3f}".format(i)) for i in probs]
        return probs_2dp, len(self.tokenizer.encode(self._text, add_special_tokens=False))
