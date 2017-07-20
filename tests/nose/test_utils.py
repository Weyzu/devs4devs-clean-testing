from nose.tools import ok_, assert_equal, assert_dict_equal

from example.utils import is_leap_year, get_user_stats, get_username


def test_is_leap_year_returns_true_for_leap_years():
    leap_years = [2016, 2020, 2024, 2028, 2400]

    for leap_year in leap_years:
        yield assert_is_leap, leap_year


def assert_is_leap(year):
    ok_(is_leap_year(year))


def test_get_user_stats_returns_full_user_statistics():
    assert_dict_equal(
        get_user_stats(username='Pinky'),
        {
            "elections_hacked": 10,
            "is_laserproof": False,
        }
    )


def test_get_username_returns_users_username():
    assert_equal(get_username(user_id=1), 'Pinky')
