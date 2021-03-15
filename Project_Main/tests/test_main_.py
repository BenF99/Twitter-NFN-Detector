import main_


def test_response():
    """ Tests that checks whether values are returned """
    tweet, fake, real, fin_url = main_.response(None, "roberta")
    assert tweet is not None and fake is not None and real is not None and fin_url is not None


def test_response_custom():
    """ Tests that checks whether values are returned for a custom input """
    fake, real = main_.response("My name is Ben", "roberta", False)
    assert fake is not None and real is not None

