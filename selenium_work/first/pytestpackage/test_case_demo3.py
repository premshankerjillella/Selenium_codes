import pytest

# allows to run same method before and after
@pytest.fixture()
def setUp():
    print("demo3 setUp")
    yield # Above this before and below this after test method
    print("demo3 tearDown")

def test_methodA(setUp):
    print("Running demo3 method A")

def test_methodB(setUp):
    print("Running demo3 method B")
