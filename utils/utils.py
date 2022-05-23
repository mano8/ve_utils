#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
from datetime import datetime


class UType(object):
    """
    Test Helper used to test and format data.

    Contain only static methods.
    """

    @staticmethod
    def is_str(value: any) -> bool:
        """
        Check if the input is a str.

        :param value: Input value to test.
        :return: True if the value is a str, otherwise False.
        """
        return isinstance(value, str)

    @staticmethod
    def is_bool(value: any) -> bool:
        """
        Check if the input is a bool.

        :param value: Input value to test.
        :return: True if the value is a bool, otherwise False.
        """
        return isinstance(value, bool)

    @staticmethod
    def is_int(value: any) -> bool:
        """
        Check if the input is a int number.

        :param value: Input value to test.
        :return: True if the value is a int number, otherwise False.
        """
        return isinstance(value, int)

    @staticmethod
    def is_float(value: any) -> bool:
        """
        Check if the input is a float number.

        :param value: Input value to test.
        :return: True if the value is a float number, otherwise False.
        """
        return isinstance(value, float)

    @staticmethod
    def is_numeric(value: any) -> bool:
        """
        Check if the input is a int number or a float number.

        :param value: Input value to test.
        :return: True if the value is a int number or a float number,
                 otherwise False.
        """
        return UType.is_int(value) or UType.is_float(value)

    @staticmethod
    def is_positive(value: any) -> bool:
        """
        Check if the input is a positive int number or a positive float number.

        :param value: Input value to test.
        :return: True if the value is a int number or a float number,
                 otherwise False.
        """
        return UType.is_numeric(value) and UType.get_float(value) > 0

    @staticmethod
    def is_negative(value: any) -> bool:
        """
        Check if the input is a negative int number or a negative float number.

        :param value: Input value to test.
        :return: True if the value is a int number or a float number,
                 otherwise False.
        """
        return UType.is_numeric(value) and UType.get_float(value) < 0

    @staticmethod
    def is_dict(value: any) -> bool:
        """
        Check if the input is a dict.

        :param value: Input value to test.
        :return: True if the value is a dict, otherwise False.
        """
        return isinstance(value, dict)

    @staticmethod
    def is_dict_not_empty(value: any) -> bool:
        """
        Check if the input is an not empty dict.

        :param value: Input value to test.
        :return: True if the value is a dict, otherwise False.
        """
        return isinstance(value, dict) and len(value) > 0

    @staticmethod
    def is_dict_key(value: any) -> bool:
        """
        Check if the input is a valid dict key.

        :param value: dict key to test.
        :return: True if the value is a valid dict key, otherwise False.
        """
        return UType.is_int(value) or\
            UType.is_str(value) or\
            UType.is_tuple(value)

    @staticmethod
    def is_tuple(value: any) -> bool:
        """
        Check if the input is a tuple.

        :param value: Input value to test.
        :return: True if the value is a Tuple, otherwise False.
        """
        return isinstance(value, tuple)

    @staticmethod
    def is_list(value: any) -> bool:
        """
        Check if the given value is a list.

        :param value: Input value to test.
        :return: True if value is a list, and False otherwise.
        """
        return isinstance(value, list)

    @staticmethod
    def is_list_not_empty(value: any) -> bool:
        """
        Check if the given value is an not empty list.

        :param value: Input value to test.
        :return: True if value is a list, and False otherwise.
        """
        return isinstance(value, list) and len(value) > 0

    @staticmethod
    def get_int(value: any, default: int or None = 0) -> int or None:
        """
        Take a value and returns it as an integer.

        :param nb: Input value to return as an integer.
        :param default=0: Used to set a default value.
        :return: the integer part of the number that is passed to it,
                 otherwise it returns the default value.
        """
        try:
            return int(value)
        except Exception:
            return default
        return default

    @staticmethod
    def get_float(value: any, default: float or None = 0.0) -> float or None:
        """
        Take a value and returns it as an float value.

        :param value: Input value to return as an float.
        :param default=0.0: Used to define the default value.
        :return: a float if the argument is a number,
                 otherwise it returns the default value.
        """
        try:
            return float(value)
        except Exception:
            return default
        return default

    @staticmethod
    def get_rounded_float(nb: any,
                          rnd: int,
                          default: float or None = 0.0
                          ) -> float or None:
        """
        Return the rounded value of a float number.

        :param nb: Used to pass the value to be rounded.
        :param rnd: Used to specify the number of digits after the comma.
        :param default=0.0: Used to specify a default value.
        :return: the rounded float value of a number,
                 otherwise it returns the default value.
        """
        try:
            return round(UType.get_float(nb), rnd)
        except Exception:
            return default
        return default

    @staticmethod
    def get_str(val: any, default: str or None = None) -> str or None:
        """
        Take a value and returns it as an str value.

        :param value: Input value to return as an str.
        :param default=0.0: Used to define the default value.
        :return: a str if the argument is a str,
                 otherwise it returns the default value.
        """
        try:
            return str(val)
        except Exception:
            return default
        return default

    @staticmethod
    def format_by_type(value: any,
                       data_type: str,
                       float_round: int or None = None
                       ):
        """
        Format value to data_type format.

        :param value: Input value to format.
        :param data_type: The data type to format the value.
        :param float_round=None:
            When data type is float,
            value can be rounded from number of decimal places.
            Defaults to None.
        :return: a formatted value, otherwise it returns None.
        """
        if data_type == "int":
            return UType.get_int(value)
        elif data_type in ["float", "numeric", "positive", "negative", "time"]:
            if float_round is not None:
                return UType.get_rounded_float(
                    UType.get_float(value),
                    float_round
                    )
            return UType.get_float(value)
        elif data_type == "onOff":
            return UType.bool_to_on_off(value)
        elif data_type == "intBool":
            return UType.string_to_int_bool(value)
        elif data_type == "bool":
            return UType.str_to_bool(value)
        elif data_type == "str":
            return UType.get_str(value)
        elif data_type == "intString":
            return UType.int_to_formatted_string(value)
        return None

    @staticmethod
    def is_valid_format(
                        value: any,
                        data_type: str,
                        default: any = None
                        ) -> bool or None:
        """
        Check if input value is an data_type format.

        :param value: Input value to test the data type.
        :param data_type: The data type to test format of the value.
        :param default=None: Used to define the default value.
        :return: True if correct data type, False if not.
                 Otherwise it returns default value, if no data type found.
        """
        if data_type == "int":
            return UType.is_int(value)
        elif data_type == "float":
            return UType.is_float(value)
        elif data_type == "numeric":
            return UType.is_numeric(value)
        elif data_type == "positive":
            return UType.is_positive(value)
        elif data_type == "negative":
            return UType.is_negative(value)
        elif data_type == "str":
            return UType.is_str(value)
        elif data_type == "bool":
            return UType.is_bool(UType.str_to_bool(value))
        elif data_type == "dict":
            return UType.is_dict(value)
        elif data_type == "dict_not_empty":
            return UType.is_dict_not_empty(value)
        elif data_type == "list":
            return UType.is_list(value)
        elif data_type == "list_not_empty":
            return UType.is_list_not_empty(value)
        return default

    @staticmethod
    def int_to_formatted_string(
            nb: int,
            default: str or None = None
            ) -> str or None:
        """
        Take an integer and returns a string with the number formatted.

        Format the number as two digits (if the number is less than 10).

        :param nb: Used to store the number that will be converted to a string.
        :return:
            a string of the number nb formatted as a two digit number
            if it is less than 10 and greater or equal to 0,
            and returns an empty string otherwise.
        """
        if UType.is_int(nb):
            if nb < 10 and nb >= 0:
                return "0%s" % (nb)
            return "%s" % (nb)
        return default

    @staticmethod
    def str_to_bool(
            s: bool or str or int,
            default: bool or None = False
            ) -> bool or None:
        """
        Convert a string or an int to a boolean.

        Todo: Change method name.
        :param s: Used to pass the value to be converted.
        :param default=False: Used to set a default value for the parameter.
        :return:
            True if the input is 'True', '1',
            or other boolean-like values.
        """
        if UType.is_bool(s):  # do not convert if already a boolean
            return s
        elif UType.is_str(s):
            if s.lower() == 'true' \
                    or s == '1' \
                    or s.lower() == 'on' \
                    or s.lower() == 'ok':
                return True
            elif s.lower() == 'false' \
                    or s == '0' \
                    or s.lower() == 'off' \
                    or s.lower() == 'error':
                return False
        elif UType.is_int(s):
            return s == 1
        return default

    @staticmethod
    def bool_to_int_text(value: bool or str or int) -> str:
        """
        Take a boolean value and returns an integer.

        :param value: Used to check if the input is a boolean value.
        :return: the value of the value parameter.
        """
        if UType.str_to_bool(value):
            return "1"
        return "0"

    @staticmethod
    def bool_to_on_off(value: bool or str or int) -> str:
        """
        Convert a boolean value to either 'on' or 'off'.

        :param value:
            Used to pass a value that is to be converted into a boolean.
        :return:
            the string "on" if the value is True
            and returns the string "off" if it's False.
        """
        if UType.str_to_bool(value):
            return "On"
        return "Off"

    @staticmethod
    def bool_to_str_state(value: bool or str or int) -> str:
        """
        Take a boolean value and returns "Ok"/"Not Ok" string.

        :param value: Used to determine if the state is 'Ok' or not.
        :return: the boolean value of the string passed to it.
        """
        if UType.str_to_bool(value):
            return "Ok"
        return "Error"

    @staticmethod
    def string_to_int_bool(text: bool or str or int) -> int:
        """
        Convert a string to an integer.

        :param text: Used to convert the string to a boolean value.
        :return:
            the integer 1 if the string is true
            and 0 if the string is false.
        """
        if UType.str_to_bool(text):
            return 1
        else:
            return 0

    @staticmethod
    def string_to_float(
            text: str,
            default: float or None = 0.0
            ) -> float or None:
        """
        Convert a string to a float.

        :param text:
            Used to pass the string that is to be converted into a float.
        :param default=0.0: Used to set a default value for the function.
        :return: the float representation of the input text string.
        """
        if UType.is_str(text):
            try:
                text = text.replace(',', '.')
                return UType.get_float(text)
            except Exception:
                return default
        elif UType.is_float(text):
            return text
        return default

    @staticmethod
    def init_dict(data: dict or None) -> dict:
        """
        Return an empty dictionary if data is not an instance of dict.

        :param data: Used to pass the property to initialyse.
        :return: An empty dictionary if data is not an instance of dict.
        """
        if not UType.is_dict(data):
            data = dict()
        return data

    @staticmethod
    def init_dict_key(
            data: dict or None,
            key: str or int or tuple,
            init_value: any
            ) -> dict:
        """
        Initialise the dictionary key value with init_value.

        If the dictionary key is not valid, raise ValueError.
        Set key value to init_value if is not an instance of init_value type.

        :param data: Used to pass the dictionary.
        :param key: Used to pass the dictionary key.
        :param init_value: Used to pass the default dictionary key value.
        :return: data with key value initialysed to default value or
                 the data param.
        """
        if not UType.is_dict_key(key):
            raise ValueError(
                "[init_dict_key] Error : dictionary key is not valid."
                )

        data = UType.init_dict(data)
        if not isinstance(data.get(key), type(init_value)):
            data[key] = init_value
        return data

    @staticmethod
    def get_keys_from_dict(data: dict, list_keys: list) -> dict:
        """
        Return a dictionary containing the keys from list_keys.

        :param data: Used to pass the dictionary to be searched.
        :param list_keys:
            Used to specify the keys,
            that we want to extract from the dictionary.
        :return: the list of keys found in the dictionary data.
        """
        res = dict()
        if UType.is_dict_not_empty(data) and UType.is_list(list_keys):
            for key in list_keys:
                if UType.is_str(key) and key in data:
                    res[key] = data.get(key)
        return res


class USys(object):
    """Sys Helper methods."""

    color_list = dict(
        PURPLE='\033[95m',
        BLUE='\033[94m',
        GREEN='\033[92m',
        YELLOW='\033[93m',
        RED='\033[91m',
        ENDLINE='\033[0m',
        BOLD='\033[1m',
        UNDERLINE='\033[4m'
    )

    @classmethod
    def pipe_print(cls, *args):
        """Print args."""
        print(*args)

    @classmethod
    def get_text_to_print(cls,
                          text_to_print: str,
                          color: str,
                          with_time=True
                          ) -> str:
        """Append formatted time to printed string."""
        res = text_to_print
        if with_time:
            res = "%s - %s" % (
                UTime.time_to_string(time.time()),
                res
                )

        if cls.color_list.get(color) is not None:
            res = "%s%s%s" % (
                cls.color_list[color],
                res,
                cls.color_list["ENDLINE"]
                )
        return res

    @classmethod
    def print_info(cls,
                   text_to_print: str,
                   with_time: bool = True
                   ) -> None:
        """Print text with info format, with BLUE color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "BLUE", with_time)
            )

    @classmethod
    def print_success(cls,
                      text_to_print: str,
                      with_time: bool = True
                      ) -> None:
        """Print text with success format, with GREEN color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "GREEN", with_time)
            )

    @classmethod
    def print_warning(cls,
                      text_to_print: str,
                      with_time: bool = True
                      ) -> None:
        """Print text with warning format, with YELLOW color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "YELLOW", with_time)
            )

    @classmethod
    def print_danger(cls,
                     text_to_print: str,
                     with_time: bool = True
                     ) -> None:
        """Print text with danger format, with YELLOW color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "RED", with_time)
            )

    @classmethod
    def print_header(cls,
                     text_to_print: str,
                     with_time: bool = True
                     ) -> None:
        """Print text with header format."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "HEADER", with_time)
            )

    @classmethod
    def print_purple(cls,
                     text_to_print: str,
                     with_time: bool = True
                     ) -> None:
        """Print text with purple color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "PURPLE", with_time)
            )

    @classmethod
    def print_bold(cls,
                   text_to_print: str,
                   with_time: bool = True
                   ) -> None:
        """Print bold text."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "BOLD", with_time)
            )

    @classmethod
    def print_underline(cls,
                        text_to_print: str,
                        with_time: bool = True
                        ) -> None:
        """Print underlined text."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "UNDERLINE", with_time)
            )

    @staticmethod
    def get_operating_system() -> str or None:
        """
        Return the operating system of the computer running this code.

        :return: the name of the operating system (Linux, MacOs or Windows).
        """
        
        platform = sys.platform
        if platform.startswith('linux') or platform.startswith('cygwin'):
            return "Linux"
        elif platform.startswith('darwin'):
            return "MacOs"
        elif platform.startswith('win'):
            return "Windows"
        else:
            raise EnvironmentError('Unsupported platform')

    @staticmethod
    def get_operating_system_type() -> str or None:
        """
        Return the operating system type.

        :return: the operating system type (unix or win32).
        """
        try:
            op = USys.get_operating_system()
            if op == "Linux" or op == "MacOs":
                return ("unix", op)
            elif op == "Windows":
                return ("win32", op)
        except Exception:
            return None
        return None

    @staticmethod
    def is_op_sys_type(sys: str) -> bool:
        """
        Return True if the operating system type is sys.

        :param sys: Used to determine the operating system type.
        :return:
            True if the operating system type is equal to sys,
            and False otherwise.
        """
        op_sys = USys.get_operating_system_type()
        return op_sys is not None and op_sys[0] == sys

    @staticmethod
    def is_op_sys(sys: str) -> bool:
        """
        Return True if the operating system is sys, and False otherwise.

        :param sys: Used to determine which operating system is being used.
        :return:
            True if the operating system is equal to sys,
            and False otherwise.
        """
        op_sys = USys.get_operating_system()
        return op_sys is not None and op_sys == sys

    @staticmethod
    def get_current_file_parent_parent_path(current_script_path: str) -> str:
        """
        Return the parent of the parent directory of this file.

        :param current_script_path: Used to get the path of the current script.
        :return: the parent of the parent of the current script's path.
        """
        return os.path.normpath(
            current_script_path + os.sep + os.pardir + os.sep + os.pardir
            )

    @staticmethod
    def get_current_file_parent_path(current_script_path: str) -> str:
        """
        Return the parent path of the current file.

        :param current_script_path: Used to get the path of the current script.
        :return: the parent path of the current script.
        """
        return os.path.normpath(
            os.path.join(current_script_path, os.pardir)
            )


class UTime(object):
    """Time Helper methods."""

    @staticmethod
    def time_to_string(
                        timeTf: int or float,
                        micro: bool = False
                        ) -> str or None:
        """
        Convert a time in seconds to a string.

        :param timeTf: Used to convert the time in seconds to a string.
        :param micro=False:
            Used to specify whether the microseconds
            should be included in the string.
        :return:
            a string representation of the time passed,
            if it is not a float then it returns None.
        """
        if UType.is_numeric(timeTf):
            try:
                date_time = datetime.fromtimestamp(timeTf)
                if micro:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S %f')
                else:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S')

            except Exception as ex:
                return None

        return None

    @staticmethod
    def get_elapsed_time(
                            tim: int or float,
                            default: int or float or None = None
                            ) -> int or float or None:
        """
        Return the elapsed time between two timestamps.

        :param tim: Used to pass in the time that is being converted.
        :param default=None:
            Used to specify a default value to return
            if the input is not an integer or float.
        :return:
            the time if it's an integer or float,
            otherwise it returns default value.
        """
        if UType.is_numeric(tim):
            return time.time()-UType.get_float(tim)
        return default

    @staticmethod
    def string_to_time(
            text: str,
            formatF: str,
            default: float or None = None
            ) -> float or None:
        """
        Convert a string to a time object.

        :param text: Used to specify the string to be converted.
        :param formatF:
            Used to specify the format of the string
            that is being converted to a time object.
        :param default=None: Used to set a default value for the function.
        :return: a time object converted from the given string and format.
        """
        if UType.is_str(text) and UType.is_str(formatF):
            try:
                return time.mktime(time.strptime(text, formatF))

            except Exception:
                return default
        return default

    @staticmethod
    def get_time_search(
            timeB: int or float,
            timeSearch: str = '23:59:59'
            ) -> int or float:
        """
        Return formated time.

        :param timeB: Used to pass the time in seconds since epoch.
        :param timeSearch='23:59:59':
            Used to set the time to 23:59:59,
            so that all logs from that day are returned.
        :return: the time search given the timeB.
        :doc-author: Trelent
        """
        if UType.is_float(timeB):
            try:
                sTime = time.gmtime(timeB)
                return time.mktime(
                    time.strptime(
                        "%s-%s-%s %s" % (
                            str(sTime[2]),
                            str(sTime[1]),
                            str(sTime[0]),
                            str(timeSearch)
                        ),
                        "%d-%m-%Y %H:%M:%S"
                    )
                )
            except Exception:
                return None
        return None
