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
    df['text'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["", ""], regex=True, inplace=True)
    return df


def add_class(type_, path):
    df = pd.read_json(path, lines=True, encoding='utf8').text.to_frame()
    df = fixnewlines(df)
    if type_ == 'real':
        df['class'] = 'human'
    else:
        df['class'] = 'machine'
    return df


def concat_dfs(df1, df2):
    df = pd.concat([df1, df2]).reset_index(drop=True)
    return df


if __name__ == '__main__':
    _dir = "C:/Users/User/Desktop/Project_Main/data/"

    train_fake = add_class('fake', f'{_dir}{"xl-1542M.train.jsonl"}')
    train_real = add_class('real', f'{_dir}{"webtext.train.jsonl"}')

    test_fake = add_class('fake', f'{_dir}{"xl-1542M.test.jsonl"}')
    test_real = add_class('real', f'{_dir}{"webtext.test.jsonl"}')

    concat_dfs(train_fake, train_real).to_pickle("train_df_500000")
    concat_dfs(test_fake, test_real).to_pickle("test_df_500000")
