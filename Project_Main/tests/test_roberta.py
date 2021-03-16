from roberta import RoBERTaClassification
import pytest


def test_text():
    """ Testing that invalid input gets caught """
    x = RoBERTaClassification()
    with pytest.raises(Exception) as excinfo:
        x.text = 123
    assert str(excinfo.value) == "Error: Invalid Input Type"


def test_add_special_tokens():
    """ Tests that speical tokens are added to tensor """
    x = RoBERTaClassification()
    tokens = [387, 2962, 523, 589]
    a = x.add_special_tokens(tokens).tolist()[0]
    tokens_st = [0, 387, 2962, 523, 589, 2]
    assert a == tokens_st


def test_check_probs():
    """ Tests check_probs return values"""
    x = RoBERTaClassification()
    x.text = "Brunel University"
    probs, tokens = x.check_probs()
    assert len(probs) == 2 and type(tokens) == int
