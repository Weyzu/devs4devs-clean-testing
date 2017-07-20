import pytest

from example.utils import is_leap_year, get_user_stats, get_username


@pytest.mark.parametrize('leap_year', [2016, 2020, 2024, 2028, 2400])
def test_is_leap_year_returns_true_for_leap_years(leap_year):
    assert is_leap_year(leap_year)


def test_get_user_stats_returns_full_user_statistics():
    assert get_user_stats(username='Pinky') == {
        "elections_hacked": 10,
        "is_laserproof": False,
    }


def test_get_username_returns_users_username():
    assert get_username(user_id=1) == 'Pinky'


def test_get_username_logs_only_on_info_level(caplog):
    get_username(user_id=1)

    assert len(caplog.records) == 1

    for record in caplog.records:
        assert record.levelname == 'INFO'
