import pytest

from xlnetdeberta import XLNetDeBERTaClassification


def test_text():
    """ Testing that invalid input gets caught """
    x = XLNetDeBERTaClassification("xlnet")
    with pytest.raises(Exception) as excinfo:
        x.text = 123
    assert str(excinfo.value) == "Error: Invalid Input Type"


def test_check_probs():
    """ Tests check_probs return values"""
    x = XLNetDeBERTaClassification("deberta")
    x.text = "Brunel University"
    probs, tokens = x.check_probs()
    assert len(probs) == 2 and type(tokens) == int
