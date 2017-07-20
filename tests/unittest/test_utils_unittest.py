from unittest import TestCase

import pytest

from example.utils import is_leap_year


@pytest.mark.skip(reason="unittest-style test")
class TestIsLeapYear(TestCase):

    def test_returns_true_for_leap_years(self):
        self.assertTrue(is_leap_year(2020))
