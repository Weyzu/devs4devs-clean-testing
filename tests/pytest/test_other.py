import pytest


@pytest.fixture
def hello():
    print('\nBefore')
    yield 'hello!'
    print('\nAfter')


def test_yield_fixtures_because_why_not(hello):
    assert hello == 'hello!'
