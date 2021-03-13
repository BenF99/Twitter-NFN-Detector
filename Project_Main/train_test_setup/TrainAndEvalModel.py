#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# =============================================================================
"""Training and testing LMs"""
# =============================================================================
# Imports
import pandas as pd
from simpletransformers.classification import ClassificationModel
import logging
from train_test_setup.lm_args import xl_args, db_args
# =============================================================================
# Suppress Certain Language Model Outputs
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)
# =============================================================================


class TrainAndEval:

    def __init__(self, model_type, model_name, model_args):
        self.train_df = pd.read_pickle("D:/Language Models/train_df_500000")
        self.eval_df = pd.read_pickle("D:/Language Models/test_df_500000")
        self.model = ClassificationModel(model_type, model_name, use_cuda=False, args=model_args)

    def train(self):
        self.model.train_model(self.train_df)

    def eval(self):
        result, model_outputs, wrong_predictions = self.model.eval_model(self.eval_df)
        print(result, model_outputs, wrong_predictions)
        return result, model_outputs, wrong_predictions


# xlnet-large-cased
xlnet = TrainAndEval("xlnet", "xlnet-large-cased", xl_args)
xlnet.train()
xlnet.eval()

# microsoft/deberta-large
deberta = TrainAndEval("deberta", "microsoft/deberta-large", db_args)
deberta.train()
deberta.eval()
