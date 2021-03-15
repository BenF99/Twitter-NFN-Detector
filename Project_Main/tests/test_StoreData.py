from StoreData import StoreData


def test_exists():
    sd = StoreData("My name is Ben", "roberta")
    assert sd.exists() is not False


def test_does_not_exist():
    sd = StoreData("(sfjda08sej83h42939h423**94873298rfsdlfnaso)", "roberta")
    assert sd.exists() is False
