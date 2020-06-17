import pytest


@pytest.fixture()
def setUp():
    print("demo1 setUp")

def test_methodA(setUp):
    print("Running demo1 method A")

def test_methodB(setUp):
    print("Running demo1 method B")
