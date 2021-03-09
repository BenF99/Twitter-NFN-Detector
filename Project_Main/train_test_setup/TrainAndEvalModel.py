#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# Date Last Updated : 09/03/2021 - 00:38
# =============================================================================
"""Training and testing LMs"""
# =============================================================================
# Imports
import pandas as pd
from simpletransformers.classification import ClassificationModel
import logging
from .lm_args import *
# =============================================================================
# Suppress Certain Language Model Outputs
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)
# =============================================================================


class TrainAndEval:

    def __init__(self, model_type, model_name, model_args):
        self.train_df = pd.read_pickle("/content/drive/MyDrive/train_df_500000")
        self.eval_df = pd.read_pickle("/content/drive/MyDrive/test_df_500000")
        self.model = ClassificationModel(model_type, model_name, use_cuda=True, args=model_args)

    def train(self):
        self.model.train_model(self.train_df)

    def eval(self):
        result, model_outputs, _ = self.model.eval_model(self.eval_df)
        return result, model_outputs


# xlnet-large-cased
xlnet = TrainAndEval("xlnet", "xlnet-large-cased", xl_args)
xlnet.train()
xlnet.eval()

# microsoft/deberta-large
xlnet = TrainAndEval("deberta", "microsoft/deberta-large", db_args)
xlnet.train()
xlnet.eval()
