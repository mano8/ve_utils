# -*- coding: utf-8 -*-
"""
UType unittest class.

Use pytest package.
"""
import pytest
from ve_utils.utype import UType as Ut


class TestUType:
    """UTime unittest class."""
    def test_has_valid_length(self):
        """Test has_valid_length method"""
        assert Ut.has_valid_length(test=True, value='tst')
        assert Ut.has_valid_length(test=True, value='tst', not_null=True)
        assert Ut.has_valid_length(test=True, value='tst', mini=1, maxi=3)
        assert Ut.has_valid_length(test=True, value='tst', mini=3, maxi=3)
        assert Ut.has_valid_length(test=True, value='tst', eq=3, mini=4, maxi=6)

        assert not Ut.has_valid_length(test=True, value='', not_null=True)
        assert not Ut.has_valid_length(test=True, value='', mini=1)
        assert not Ut.has_valid_length(test=True, value='aaa', maxi=1)
        assert not Ut.has_valid_length(test=False, value='tst')

        with pytest.raises(AttributeError):
            Ut.has_valid_length(test=True, value='tst', mini=-1, maxi=2)

        with pytest.raises(AttributeError):
            Ut.has_valid_length(test=False, value='tst', mini=-1, maxi=2)

        with pytest.raises(AttributeError):
            Ut.has_valid_length(test=False, value='tst', mini=0, maxi=0)

        with pytest.raises(AttributeError):
            Ut.has_valid_length(test=False, value='tst', mini=5, maxi=2)

        with pytest.raises(AttributeError):
            Ut.has_valid_length(test=False, value='tst', eq=-1)

        with pytest.raises(TypeError):
            assert Ut.has_valid_length(test=True, value=None, not_null=True)

    def test_has_valid_value(self):
        """Test has_valid_value method"""
        assert Ut.has_valid_value(test=True, value=1)
        assert Ut.has_valid_value(test=True, value=-2, not_null=True)
        assert Ut.has_valid_value(test=True, value=1, mini=1, maxi=3)
        assert Ut.has_valid_value(test=True, value=3, mini=3, maxi=3)
        assert Ut.has_valid_value(test=True, value=3, eq=3)
        assert Ut.has_valid_value(test=True, value=3, positive=True)
        assert Ut.has_valid_value(test=True, value=-3, negative=True)

        assert not Ut.has_valid_value(test=True, value=0, not_null=True)
        assert not Ut.has_valid_value(test=True, value=-1, mini=1)
        assert not Ut.has_valid_value(test=True, value=2, maxi=1)
        assert not Ut.has_valid_value(test=True, value=2, eq=1)
        assert not Ut.has_valid_value(test=True, value=0, positive=True)
        assert not Ut.has_valid_value(test=True, value=-1, positive=True)
        assert not Ut.has_valid_value(test=True, value=0, negative=True)
        assert not Ut.has_valid_value(test=True, value=2, negative=True)
        assert not Ut.has_valid_value(test=False, value=1)

        with pytest.raises(AttributeError):
            Ut.has_valid_value(test=True, value=3, eq=3, mini=-1, maxi=2)

        with pytest.raises(AttributeError):
            Ut.has_valid_value(test=False, value=3, eq=3, maxi=2)

        with pytest.raises(AttributeError):
            Ut.has_valid_value(test=False, value=3, eq=3, mini=2)

        with pytest.raises(AttributeError):
            Ut.has_valid_value(test=False, value=3, eq=-3, not_null=True)

        with pytest.raises(AttributeError):
            Ut.has_valid_value(test=False, value=3, mini=5, maxi=2)

        with pytest.raises(TypeError):
            Ut.has_valid_value(test=True, value='tst', mini=-1)

        with pytest.raises(TypeError):
            assert Ut.has_valid_value(test=True, value=None, maxi=2)

    def test_is_str(self):
        """Test is_str method"""
        datas = [
            '_hy', 'hy', "#hj_58 Hyufdgdfi#", "hj_58Hyui", "",  # true
            -1, True, dict(), list(), None  # false
        ]
        tests = [x for x in datas if Ut.is_str(value=x, mini=3, maxi=10)]
        assert len(tests) == 2

        tests = [x for x in datas if Ut.is_str(value=x, not_null=True, maxi=10)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_str(value=x, not_null=True)]
        assert len(tests) == 4

        tests = [x for x in datas if Ut.is_valid_format(value=x, data_type='str', not_null=True)]
        assert len(tests) == 4

        tests = [x for x in datas if Ut.is_valid_format(value=x, data_type=str)]
        assert len(tests) == 5

    def test_is_bool(self):
        """Test is_bool method"""
        datas = [
            True, False,  # true
            0, 1, "hello", dict(), list()  # false
        ]
        tests = [x for x in datas if Ut.is_bool(x)]
        assert len(tests) == 2

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='bool')]
        assert len(tests) == 2

        tests = [x for x in datas if Ut.is_valid_format(x, data_type=bool)]
        assert len(tests) == 2

    def test_is_int(self):
        """Test is_int method"""
        datas = [
            0, 0x235, -999999999999999999999999999999999999999999999999999999, 5,
            -2, -6, True, False,  # true
            '_hello', dict(), list(), 0.1  # false
        ]
        tests = [x for x in datas if Ut.is_int(value=x, not_null=True, mini=-3, maxi=10)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_int(value=x, mini=-3, maxi=10)]
        assert len(tests) == 5

        tests = [x for x in datas if Ut.is_int(value=x, maxi=10)]
        assert len(tests) == 7

        tests = [x for x in datas if Ut.is_int(value=x, mini=-6)]
        assert len(tests) == 7

        tests = [x for x in datas if Ut.is_valid_format(x, data_type=int, mini=-3, maxi=10)]
        assert len(tests) == 5

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='int')]
        assert len(tests) == 8

    def test_is_float(self):
        """Test is_float method"""
        datas = [
            0.0, -100.1, -999999999999999999999999999999999999999999999999999999.2,  # true
            5.1, -2.6, -6.5,
            '_hello', True, dict(), list(), 0  # false
        ]
        tests = [x for x in datas if Ut.is_float(value=x, not_null=True, mini=-100.1, maxi=10)]
        assert len(tests) == 4

        tests = [x for x in datas if Ut.is_float(value=x, mini=-6.5, maxi=5.1)]
        assert len(tests) == 4

        tests = [x for x in datas if Ut.is_float(value=x, maxi=5)]
        assert len(tests) == 5

        tests = [x for x in datas if Ut.is_float(value=x, mini=-6.5)]
        assert len(tests) == 4

        tests = [x for x in datas if Ut.is_valid_format(x, data_type=float, mini=-6.5)]
        assert len(tests) == 4

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='float')]
        assert len(tests) == 6

    def test_is_numeric(self):
        """Test is_numeric method"""
        datas = [
            0, 0x235, -999999999999999999999999999999999999999999999999999999, 5,  # true
            -2, -6, True, False,  # true
            0.0, -100.1, -999999999999999999999999999999999999999999999999999999.2,  # true
            5.1, -2.6, -6.5,
            '_hello', dict(), list()  # false
        ]
        tests = [x for x in datas if Ut.is_numeric(value=x, not_null=True, mini=-100.1, maxi=10)]
        assert len(tests) == 8

        tests = [x for x in datas if Ut.is_numeric(value=x, mini=-6.5, maxi=5.1)]
        assert len(tests) == 10

        tests = [x for x in datas if Ut.is_numeric(value=x, not_null=True, mini=-3, maxi=10)]
        assert len(tests) == 5

        tests = [x for x in datas if Ut.is_numeric(value=x, mini=-3, maxi=10)]
        assert len(tests) == 8

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='numeric', mini=-3, maxi=10)]
        assert len(tests) == 8

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='numeric')]
        assert len(tests) == 14

    def test_is_dict(self):
        """Test is_dict method"""
        datas = [
            dict(), {0: "0", 1: "1", 2: "2", 3: "3"}, {"a": "0", "b": "0"}, {(1, 0): "0"},  # true
            0.0, 1.1, "hello", tuple(), list()  # false
        ]

        tests = [x for x in datas if Ut.is_dict(x, not_null=True, min_items=1)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_dict(x, not_null=True, min_items=2)]
        assert len(tests) == 2

        tests = [x for x in datas if Ut.is_dict(x, min_items=1, max_items=2)]
        assert len(tests) == 2

        with pytest.raises(AttributeError):
            Ut.is_dict({}, min_items=-1, max_items=2)

        tests = [x for x in datas if Ut.is_valid_format(x, data_type=dict, not_null=True)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='dict')]
        assert len(tests) == 4

    def test_is_tuple(self):
        """"""
        datas = [
            tuple(), (0, 1, 2), (0, 1, 2, 3), ('a', 'b'),  # true
            0.0, 1.1, "hello", list(), dict()  # false
        ]

        tests = [x for x in datas if Ut.is_tuple(x, not_null=True, min_items=2)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_tuple(x, min_items=3)]
        assert len(tests) == 2

        tests = [x for x in datas if Ut.is_tuple(x, max_items=3)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_valid_format(x, data_type=tuple, not_null=True)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='tuple')]
        assert len(tests) == 4

    def test_is_list(self):
        """Test is_list method"""
        datas = [
            list(), [0, 1, 2, 3, 4], [1, "0"], [(1, 0), "0"],  # true
            0.0, 1.1, "hello", tuple(), dict()  # false
        ]

        tests = [x for x in datas if Ut.is_list(x, max_items=3)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_list(x, min_items=3)]
        assert len(tests) == 1

        tests = [x for x in datas if Ut.is_valid_format(x, data_type=list, not_null=True)]
        assert len(tests) == 3

        tests = [x for x in datas if Ut.is_valid_format(x, data_type='list')]
        assert len(tests) == 4

    def test_is_valid_format(self):
        """Test is_valid_format method"""
        with pytest.raises(AttributeError):
            Ut.is_valid_format({}, data_type="bad data type")
        assert Ut.is_list(Ut.get_valid_data_types_test())

    def test_get_int(self):
        """Test get_int method"""
        assert Ut.get_int("hello", 0) == 0
        assert Ut.get_int(0.1) == 0
        assert Ut.get_int("bg", 2) == 2
        assert Ut.get_int(True) == 1
        assert Ut.get_int([]) == 0

    def test_get_float(self):
        """Test get_float method"""
        assert Ut.get_float("hello", 0.0) == 0.0
        assert Ut.get_float(0.1) == 0.1
        assert Ut.get_float("bg", 2.5) == 2.5
        assert Ut.get_float(True) == 1.0
        assert Ut.get_float([]) == 0.0

    def test_get_rounded_float(self):
        """Test get_rounded_float method"""
        assert Ut.get_rounded_float("hello", 1, 0.156) == 0.0
        assert Ut.get_rounded_float(0.1665616, 3) == 0.167
        assert Ut.get_rounded_float("bg", 2, 2.589898) == 0.0
        assert Ut.get_rounded_float(None, dict(), None) is None

    def test_get_str(self):
        """Test get_str method"""
        assert Ut.get_str("hello") == "hello"
        assert Ut.get_str(0.1665616) == "0.1665616"
        assert Ut.get_str(10) == "10"
    
    def test_format_by_type(self):
        """Test format_by_type method"""
        assert Ut.format_by_type("32", 'int') == 32
        assert Ut.format_by_type("32", 'float') == 32.0
        assert Ut.format_by_type(32, 'str') == '32'
        assert Ut.format_by_type(1, 'bool') is True
        assert Ut.format_by_type(True, 'onOff') == 'On'
        assert Ut.format_by_type(False, 'onOff') == 'Off'
        assert Ut.format_by_type(True, 'intBool') == 1
        assert Ut.format_by_type(False, 'intBool') == 0
        assert Ut.format_by_type(1.25698789, 'float', 3) == 1.257
        assert Ut.format_by_type(8, 'intString') == "08"
        assert Ut.format_by_type(10, 'intString') == "10"
        with pytest.raises(AttributeError):
            Ut.format_by_type({}, data_type="bad data type")

    def test_int_to_formatted_string(self):
        """Test int_to_formatted_string method"""
        assert Ut.int_to_formatted_string(0) == "00"
        assert Ut.int_to_formatted_string(5) == "05"
        assert Ut.int_to_formatted_string(10) == "10"
        assert Ut.int_to_formatted_string(125) == "125"
        assert Ut.int_to_formatted_string("bad") is None
        assert Ut.int_to_formatted_string("bad", False) is False

    def test_str_to_bool(self):
        """Test str_to_bool method"""
        assert Ut.str_to_bool("true")
        assert Ut.str_to_bool("1")
        assert Ut.str_to_bool("On")
        assert Ut.str_to_bool("Ok")
        assert Ut.str_to_bool(1)
        assert Ut.str_to_bool(True)
        assert not Ut.str_to_bool("False")
        assert not Ut.str_to_bool("0")
        assert not Ut.str_to_bool("Off")
        assert not Ut.str_to_bool("Error")
        assert not Ut.str_to_bool(0)
        assert not Ut.str_to_bool(False)
        assert Ut.str_to_bool(None, None) is None

    def test_bool_to_int_text(self):
        """Test bool_to_int_text method"""
        assert Ut.bool_to_int_text(True) == "1"
        assert Ut.bool_to_int_text(False) == "0"

    def test_bool_to_on_off(self):
        """Test bool_to_on_off method"""
        assert Ut.bool_to_on_off(True) == "On"
        assert Ut.bool_to_on_off(False) == "Off"

    def test_bool_to_str_state(self):
        """Test bool_to_str_state method"""
        assert Ut.bool_to_str_state(True) == "Ok"
        assert Ut.bool_to_str_state(False) == "Error"

    def test_string_to_int_bool(self):
        """Test string_to_int_bool method"""
        assert Ut.string_to_int_bool(True) == 1
        assert Ut.string_to_int_bool(False) == 0

    def test_string_to_float(self):
        """Test string_to_float method"""
        assert Ut.string_to_float('0,125') == 0.125
        assert Ut.string_to_float('0.125') == 0.125
        assert Ut.string_to_float(0.125) == 0.125
        assert Ut.string_to_float(None, None) is None

    def test_init_dict(self):
        """Test init_dict method"""
        assert Ut.init_dict('0,125') == dict()
        assert Ut.init_dict({'a': 0}) == {'a': 0}

    def test_init_dict_key(self):
        """Test init_dict_key method"""
        assert Ut.init_dict_key(dict(), 'my_key', list()) == {'my_key': list()}
        assert Ut.init_dict_key(dict(), 'my_key', dict()) == {'my_key': dict()}
        with pytest.raises(ValueError):
            assert Ut.init_dict_key(dict(), None, dict())

    def test_get_items_from_dict(self):
        """Test init_dict_key method"""
        data = {
            'a': 0, 'b': 1, 'c': 2
        }
        assert Ut.get_items_from_dict(data, ['a']) == {'a': 0}
        assert Ut.get_items_from_dict(data, ['a', 'c']) == {'a': 0, 'c': 2}
