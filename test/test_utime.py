import pytest
import time
from ve_utils.utils import UType as U
from ve_utils.utils import UTime

class TestUtils():

    def test_get_elapsed_time(self):
        """"""
        assert UTime.get_elapsed_time(32) <= U.get_int(time.time()+32)
    
    def test_time_to_string(self):
        """"""
        assert UTime.time_to_string(1630193115.6428988) == '29/08/2021 01:25:15'
        assert UTime.time_to_string(1630193115.6428988, True) == '29/08/2021 01:25:15 642899'

    def test_string_to_time(self):
        """"""
        assert UTime.string_to_time('29/08/2021', '%d/%m/%Y') == 1630188000.0 
    
    def test_get_time_search(self):
        """"""
        assert UTime.get_time_search(1630188000.0, '10:12:58') == 1630138378.0
