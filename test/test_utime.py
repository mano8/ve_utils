import time
from ve_utils.utype import UType as Ut
from ve_utils.utime import UTime


class TestUTime:

    def test_time_to_string(self):
        """"""
        assert UTime.time_to_string(
            UTime.get_utc_timestamp(1630193115.6428988)
        ) == '28/08/2021 23:25:15'
        assert UTime.time_to_string(
            UTime.get_utc_timestamp(1630193115.6428988),
            True
        ) == '28/08/2021 23:25:15 642899'

    def test_get_elapsed_time(self):
        """"""
        assert UTime.get_elapsed_time(32) <= Ut.get_int(time.time() + 32)

    def test_string_to_time(self):
        """"""
        assert UTime.get_utc_timestamp(
            UTime.string_to_time('29/08/2021', '%d/%m/%Y')
        ) == 1630180800.0
    
    def test_get_time_search(self):
        """"""
        assert UTime.get_utc_timestamp(
            UTime.get_time_search(1630188000.0, '10:12:58')
        ) == 1630131178.0
