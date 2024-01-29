# app.py
# This is a test commit
def add(a, b, c):
    return a + b + c

def test_add():
    assert add(1, 2, 4) == 7
    assert add(1, -1, 0) == 0
