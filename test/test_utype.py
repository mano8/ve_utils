import pytest
from ve_utils.utils import UType as U

class TestUtils():

    def test_is_str(self):
        """"""
        assert U.is_str("hello")
        assert U.is_str("")
        assert not U.is_str(0)
        assert not U.is_str(True)
        assert not U.is_str({})
        assert not U.is_str([])
    
    def test_is_bool(self):
        """"""
        assert not U.is_bool("hello")
        assert not U.is_bool(0)
        assert U.is_bool(True)
        assert U.is_bool(False)
        assert not U.is_bool([])
    
    def test_is_int(self):
        """"""
        assert not U.is_int("hello")
        assert U.is_int(0)
        assert not U.is_int(1.2)
        assert U.is_int(0x235)
        assert U.is_int(True)
        assert not U.is_int([])

    def test_is_float(self):
        """"""
        assert not U.is_float("hello")
        assert U.is_float(0.1)
        assert not U.is_float(0)
        assert not U.is_float(True)
        assert not U.is_float([])

    def test_is_numeric(self):
        """"""
        assert not U.is_numeric("hello")
        assert U.is_numeric(0.1)
        assert U.is_numeric(0)
        assert U.is_numeric(True)
        assert not U.is_numeric([])
    
    def test_is_dict(self):
        """"""
        assert not U.is_dict("hello")
        assert not U.is_dict(0.1)
        assert not U.is_dict(0)
        assert not U.is_dict(True)
        assert not U.is_dict([])
        assert U.is_dict({})
    
    def test_is_tuple(self):
        """"""
        assert not U.is_tuple("hello")
        assert not U.is_tuple(0.1)
        assert not U.is_tuple(0)
        assert not U.is_tuple(True)
        assert not U.is_tuple([])
        assert U.is_tuple((0,1))
        assert not U.is_tuple({})

    def test_is_list(self):
        """"""
        assert not U.is_list("hello")
        assert not U.is_list(0.1)
        assert not U.is_list(0)
        assert not U.is_list(True)
        assert U.is_list([])
        assert not U.is_list((0,1))
        assert not U.is_list({})
    
    def test_get_int(self):
        """"""
        assert U.get_int("hello", 0) == 0
        assert U.get_int(0.1) == 0
        assert U.get_int("bg", 2) == 2
        assert U.get_int(True) == 1
        assert U.get_int([]) == 0

    def test_get_float(self):
        """"""
        assert U.get_float("hello", 0.0) == 0.0
        assert U.get_float(0.1) == 0.1
        assert U.get_float("bg", 2.5) == 2.5
        assert U.get_float(True) == 1.0
        assert U.get_float([]) == 0.0

    def test_get_rounded_float(self):
        """"""
        assert U.get_rounded_float("hello", 1, 0.156) == 0.0
        assert U.get_rounded_float(0.1665616, 3) == 0.167
        assert U.get_rounded_float("bg", 2, 2.589898) == 0.0

    def test_get_str(self):
        """"""
        assert U.get_str("hello") == "hello"
        assert U.get_str(0.1665616) == "0.1665616"
        assert U.get_str(10) == "10"
    
    def test_format_by_type(self):
        """"""
        assert U.format_by_type(32, 'str') == '32'
        assert U.format_by_type(True, 'onOff') == 'On'
        assert U.format_by_type(False, 'onOff') == 'Off'
        assert U.format_by_type(True, 'intBool') == 1
        assert U.format_by_type(False, 'intBool') == 0
        assert U.format_by_type(1.25698789, 'float', 3) == 1.257
        assert U.format_by_type(8, 'intString') == "08"
        assert U.format_by_type(10, 'intString') == "10"

    def test_string_to_float(self):
        """"""
        assert U.string_to_float('0,125') == 0.125
        assert U.string_to_float('0.125') == 0.125

    def test_str_to_bool(self):
        """"""
        assert U.str_to_bool("true")
        assert U.str_to_bool("1")
        assert U.str_to_bool("On")
        assert U.str_to_bool("Ok")
        assert U.str_to_bool(1)
        assert U.str_to_bool(True)
        assert not U.str_to_bool("False")
        assert not U.str_to_bool("0")
        assert not U.str_to_bool("Off")
        assert not U.str_to_bool("Error")
        assert not U.str_to_bool(0)
        assert not U.str_to_bool(False)
