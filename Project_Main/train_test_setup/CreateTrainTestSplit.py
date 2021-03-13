#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben Feigenbaum
# =============================================================================
"""Creating training and testing dataset for training and evaluation"""
# =============================================================================
# Imports
import pandas as pd
# =============================================================================


def fixnewlines(df):
    return df['text'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["", ""], regex=True, inplace=True)


def createdataset(pkl_name, machine, human):
    df1 = pd.read_json(machine, lines=True, encoding='utf8').text.to_frame()
    df2 = pd.read_json(human, lines=True, encoding='utf8').text.to_frame()

    df1, df2 = fixnewlines(df1), fixnewlines(df2)
    df1['class'], df2['class'] = 'machine', 'human'

    df = pd.concat([df1, df2]).reset_index(drop=True)
    df.columns = ["text", "labels"]
    df.to_pickle(pkl_name)


_dir = "C:/Users/User/Desktop/Project_Main/data/"
createdataset("test_df_500000", f'{_dir}{"xl-1542M.test.jsonl"}', f'{_dir}{"webtext.test.jsonl"}')
createdataset("train_df_500000", f'{_dir}{"xl-1542M.train.jsonl"}', f'{_dir}{"webtext.train.jsonl"}')
