from git_workflows.main import hello, add


def test_hello():
    assert hello() == "Hello, World!"


def test_add():
    assert add(1, 2) == 3
