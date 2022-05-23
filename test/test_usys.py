import pytest
import time
from utils.utils import UType as U
from utils.utils import USys as USys

class TestUSys():    
    
    def test_get_operating_system(self):
        """"""
        assert U.is_str(USys.get_operating_system())
    
    def test_get_operating_system_type(self):
        """"""
        assert U.is_tuple(USys.get_operating_system_type())

