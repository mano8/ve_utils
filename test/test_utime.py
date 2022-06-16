# -*- coding: utf-8 -*-
"""
UTime unittest class.

Use pytest package.
"""
import time
from datetime import datetime
from ve_utils.utype import UType as Ut
from ve_utils.utime import UTime


class TestUTime:
    """UTime unittest class."""
    def test_get_timestamp_from_datetime(self):
        """Test get_timestamp_from_datetime method"""
        assert UTime.get_timestamp_from_datetime(None) is None
        assert Ut.is_float(UTime.get_timestamp_from_datetime(datetime.now()))

    def test_time_to_string(self):
        """Test time_to_string method"""
        assert UTime.time_to_string(
            UTime.get_utc_timestamp(1630193115.6428988)
        ) == '28/08/2021 23:25:15'
        assert UTime.time_to_string(
            UTime.get_utc_timestamp(1630193115.6428988),
            True
        ) == '28/08/2021 23:25:15 642899'
        assert UTime.time_to_string(None) is None
        assert UTime.time_to_string(99999999999999999999999999999999999999999999999999999999999999999999999999) is None

    def test_get_elapsed_time(self):
        """Test get_elapsed_time method"""
        assert UTime.get_elapsed_time(32) <= Ut.get_int(time.time() + 32)
        assert UTime.get_elapsed_time(None) is None

    def test_string_to_time(self):
        """Test string_to_time method"""
        assert Ut.is_float(
            UTime.get_utc_timestamp(
                UTime.string_to_time('29/08/2021', '%d/%m/%Y')
            ),
            not_null=True
        )
        assert UTime.string_to_time('hello', 'world') is None
        assert UTime.string_to_time(dict(), list()) is None
    
    def test_get_time_search(self):
        """Test get_time_search method"""
        assert Ut.is_float(
            UTime.get_utc_timestamp(
                UTime.get_time_search(1630188000.0, '10:12:58')
            ),
            not_null=True
        )
        assert UTime.get_time_search(None) is None
        assert UTime.get_time_search(
            99999999999999999999999999999999999999999999999999999999999999999999999999999999999.99
        ) is None
