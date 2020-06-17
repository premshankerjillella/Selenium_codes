import pytest

# allows to run same method before and after
@pytest.fixture()
def setUp():
    print("demo2 setUp")
    yield # Above this before and below this after test method
    print("demo2 tearDown")

def test_methodA(setUp):
    print("Running demo2 method A")

def test_methodB(setUp):
    print("Running demo2 method B")
