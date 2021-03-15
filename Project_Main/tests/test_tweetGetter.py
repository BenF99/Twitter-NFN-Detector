from tweetGetter import TweetGetter


def test_getrecentweet():
    """Test to check that news related tweet is returned"""
    t = TweetGetter()
    id_, ht = t.getrecentweet(None)
    assert type(id_) == str and ht == "News"


def test_getrecentweet_custom():
    """Test to check that custom tweet related tweet is returned"""
    t = TweetGetter()
    id_, ht = t.getrecentweet("#football")
    assert type(id_) == str and ht == "#football"


def test_gettweetdata():
    """Test to check that three string parameters are returned"""
    t = TweetGetter()
    id_, _ = t.getrecentweet(None)
    t.tweet = id_
    tweet, text, fin_url = t.gettweetdata(t.tweet)
    assert type(tweet) == str and type(text) == str and type(fin_url) == str
