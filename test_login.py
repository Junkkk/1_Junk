import pytest
import time
import random

from login import login, re_login


TEST_CASE = {'aaaaaaaaaaaaaaaaaaaaa': False,
             'a': False,
             '': False,
             'As-df.asdF': True,
             'asdf.': False,
             '---.----A': False,
             'A---.----A': True
             }


@pytest.fixture()
def resource_setup(request):
    start_time = time.monotonic()

    def resource_teardown():
        print(f'\nПрошло {time.monotonic() - start_time}')
    request.addfinalizer(resource_teardown)


def test_login_performance(resource_setup):

    for _ in range(1000000):
        login(random.choice([k for k in TEST_CASE.keys()]))


def test_re_login_performance(resource_setup):
    for _ in range(1000000):
        re_login(random.choice([k for k in TEST_CASE.keys()]))


def test_login_correct():
    for case, ans in TEST_CASE.items():
        assert login(case) == ans
        assert re_login(case) == ans
