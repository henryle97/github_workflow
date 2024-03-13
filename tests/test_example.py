def test_demo():
    assert 1 + 1 == 2


def test_bad_code():
    message = "Hello World"
    words = message.split(" ")
    assert len(words) == 1
