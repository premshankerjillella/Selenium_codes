import pytest

# allows to run same method before and after
@pytest.fixture()
def setUp():
    print("conftest - demo method setUp")
    yield # Above this before and below this after test method
    print("conftest - demo method tearDown")

@pytest.fixture(scope="module")  # this runs before and after every module not method
def oneTimeSetUp():
    print("conftest - one time setUp")
    yield # Above this before and below this after test method
    print("conftest - one time tearDown")