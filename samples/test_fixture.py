import pytest


@pytest.fixture()
def setup():
    print('test start')
    yield
    print('test ends')


def testcase01(setup):
    print('This is testcase01')
    assert 2 == 1+1


if __name__ == '__main__':
    pytest.main(['-s', '-v'])

