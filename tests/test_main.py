from git_workflows.main import hello, add, multiply


def test_hello():
    assert hello() == "Hello, World!"


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2, 3) == 6

