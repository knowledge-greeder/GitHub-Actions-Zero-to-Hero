# app.py
# This is a test commit for new checks 
def add(a, b):
    return a + b 

def test_add():
    assert add(1, 2) == 7
    assert add(1, -1) == 0
