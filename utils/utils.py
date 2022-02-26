#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
import datetime

class UType(object):

    @staticmethod
    def is_str(value):
        """ 
        Checks if the input is a str.

        :param value: Input value to test.
        :return: True if the value is a str, otherwise False.
        """        
        return (type(value) is str)

    @staticmethod
    def is_bool(value):
        """ 
        Checks if the input is a bool.

        :param value: Input value to test.
        :return: True if the value is a bool, otherwise False.
        """   
        return (type(value) is bool)
    
    @staticmethod
    def is_int(value):
        """ 
        Checks if the input is a int number.

        :param value: Input value to test.
        :return: True if the value is a int number, otherwise False.
        """
        return (type(value) is int)
    
    @staticmethod
    def is_float(value):
        """
        Checks if the input is a float number.

        :param value: Input value to test.
        :return: True if the value is a float number, otherwise False.
        """
        return (type(value) is float)
    
    @staticmethod
    def is_numeric(value):
        """
        Checks if the input is a int number or a float number.

        :param value: Input value to test.
        :return: True if the value is a int number or a float number, otherwise False.
        """
        return (UType.is_int(value) or UType.is_float(value))
    
    @staticmethod
    def is_dict(value):
        """
        Checks if the input is a dict.

        :param value: Input value to test.
        :return: True if the value is a dict, otherwise False.
        """
        return (type(value) is dict)

    @staticmethod
    def is_tuple(value):
        """
        Checks if the input is a tuple.

        :param value: Input value to test.
        :return: True if the value is a Tuple, otherwise False.
        """
        return (type(value) is tuple)


    @staticmethod
    def is_list(value):
        """
        Checks if the given value is a list.

        :param value: Input value to test.
        :return: True if value is a list, and False otherwise.
        """
        return (type(value) is list)


    @staticmethod
    def get_int(value, default = 0):
        """
        Takes a value and returns it as an integer.

        :param nb: Input value to return as an integer.
        :param default=0: Used to set a default value for the variable 'nb' if it is not an integer.
        :return: the integer part of the number that is passed to it, otherwise it returns the default value.
        """
        try:
            return int(value)
        except Exception:
            return default
        return default
    
    @staticmethod
    def get_float(value, default = 0.0):
        """
        Takes a value and returns it as an float value.

        :param value: Input value to return as an float.
        :param default=0.0: Used to define the default value of the variable 'value' if it is not a float.
        :return: a float if the argument is a number, otherwise it returns the default value.
        """
        try:
            return float(value)
        except Exception:
            return default
        return default
    
    @staticmethod
    def get_rounded_float(nb, rnd, default = 0.0):
        """
        The getRoundedFloat function returns the rounded value of a float number.
        
        :param nb: Used to pass the value to be rounded.
        :param rnd: Used to specify the number of digits after the comma.
        :param default=0.0: Used to specify a default value for the 'rnd' parameter.
        :return: the rounded float value of a number, otherwise it returns the default value.
        """
        try:
            return round(UType.get_float(nb), rnd)
        except Exception:
            return default
        return default
    
    
    @staticmethod
    def get_str(val, default = None):
        """
        Takes a value and returns it as an str value.

        :param value: Input value to return as an str.
        :param default=0.0: Used to define the default value of the variable 'value' if it is not a str.
        :return: a str if the argument is a str, otherwise it returns the default value.
        """
        try:
            return str(val)
        except Exception:
            return default
        return default
    
    @staticmethod
    def format_by_type(value, data_type, float_round=None):
        """
        Format value to data_type format

        :param value: Input value to format.
        :param data_type: The data type to format the value.
        :param float_round=None: When data type is float, value can be rounded from number of decimal places. Defaults to None.
        :return: a formatted value, otherwise it returns None.
        """
        if data_type == "int":
            return UType.get_int(value)
        elif data_type == "float":
            if float_round is not None:
                return UType.get_rounded_float(UType.get_float(value), float_round)
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
    def is_valid_format(value, data_type, default = None):
        """
        Checks if input value is an data_type format

        :param value: Input value to test the data type.
        :param data_type: The data type to test format of the value.
        :param default=None: Used to define the default value of the variable 'value' if it is not a valid data type.
        :return: True if correct data type, False if not. Otherwise it returns default value, if no data type found.
        """
        if data_type == "int":
            return UType.is_int(value)
        elif data_type == "float":
            return UType.is_float(value)
        elif data_type == "str":
            return UType.is_str(value)
        elif data_type == "bool":
            return UType.is_bool(UType.str_to_bool(value))
        elif data_type == "dict":
            return UType.is_dict(value)
        elif data_type == "list":
            return UType.is_list(value)
        return default
    
    @staticmethod
    def int_to_formatted_string(nb):
        """
        Takes an integer and returns a string with the number formatted as two digits (if the number is less than 10).
        
        :param nb: Used to store the number that will be converted to a string.
        :return: a string of the number nb formatted as a two digit number if it is less than 10 and greater or equal to 0, and returns an empty string otherwise.
        """
        if UType.is_int(nb):
            if nb < 10 and nb >= 0:
                return "0%s"%(nb)
            return "%s"%(nb)
        return None
    
    @staticmethod
    def str_to_bool(s, default=False):
        """
        Converts a string or an int to a boolean.
        
        :param s: Used to pass the value to be converted.
        :param default=False: Used to set a default value for the parameter.
        :return: True if the input is 'True', '1', or other boolean-like values.
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
    def bool_to_int_text(value):
        """
        Takes a boolean value and returns an integer.
        
        :param value: Used to check if the input is a boolean value.
        :return: the value of the value parameter.
        """
        if UType.str_to_bool(value):
            return "1"
        return "0"
    
    @staticmethod
    def bool_to_on_off(value):
        """
        Converts a boolean value to either 'on' or 'off'.
        
        :param value: Used to pass a value that is to be converted into a boolean.
        :return: the string "on" if the value is True and returns the string "off" if it's False.
        """
        if UType.str_to_bool(value):
            return "On"
        return "Off"

    @staticmethod
    def bool_to_str_state(value):
        """
        Takes a boolean value and returns the string "Ok" if True, or "Not Ok" if False.
        
        :param value: Used to determine if the state is 'Ok' or not.
        :return: the boolean value of the string passed to it.
        """
        if UType.str_to_bool(value):
            return "Ok"
        return "Error"

    @staticmethod
    def string_to_int_bool(text):
        """
        Converts a string to an integer.
        
        :param text: Used to convert the string to a boolean value.
        :return: the integer 1 if the string is true and 0 if the string is false.
        """
        if UType.str_to_bool(text):
            return 1
        else:
            return 0
    
    @staticmethod
    def string_to_float(text, default=0.0):
        """
        Converts a string to a float.
        
        :param text: Used to pass the string that is to be converted into a float.
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
    def get_keys_from_dict(data, list_keys):
        """
        Returns a dictionary containing the keys from the input dictionary that are in the list of keys.
        
        :param data: Used to pass the dictionary to be searched.
        :param list_keys: Used to specify the keys that we want to extract from the dictionary.
        :return: the list of keys found in the dictionary data.
        """
        res = dict()
        if UType.is_dict(data) and UType.is_list(list_keys):

            for key in list_keys:
                if UType.is_str(key) and key in data:
                    res[key] = data.get(key)
        return res


def pipe_print(line):
    print(line)


class USys(object):
    
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

    ##################
    #
    # Shell properly displayed
    #
    #########
    @classmethod
    def get_text_to_print(cls, text_to_print, with_time=True):
        if with_time: 
            return "%s - %s"%(UTime.time_to_string(time.time()), text_to_print)
        return text_to_print    
        
    @classmethod
    def print_info(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["BLUE"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @classmethod
    def print_success(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["GREEN"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @classmethod
    def print_warning(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["YELLOW"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @classmethod
    def print_danger(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["RED"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @classmethod
    def print_header(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["HEADER"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @classmethod
    def print_purple(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["PURPLE"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @classmethod
    def print_bold(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["BOLD"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @classmethod
    def print_underline(cls, text_to_print, with_time=True):
        pipe_print(cls.color_list["UNDERLINE"] + USys.get_text_to_print(text_to_print, with_time) + cls.color_list["ENDLINE"])

    @staticmethod
    def get_operating_system():
        """
        Returns the operating system of the computer running this code.
        
        :return: the name of the operating system (Linux, MacOs or Windows).
        """
        try:
            platform = sys.platform
            if platform == "linux" or platform == "linux2":
                return "Linux"
            elif platform == "darwin":
                return "MacOs"
            elif platform == "win32":
                return "Windows"
        except Exception as ex:
            return None
        return None
    
    @staticmethod
    def get_operating_system_type():
        """
        Returns the operating system type.
        
        :return: the operating system type (unix or win32).
        """
        try:
            op = USys.getOperatingSystem()
            if op == "Linux" or op == "MacOs":
                return ("unix", op)
            elif op == "Windows":
                return ("win32", op)
        except Exception as ex:
            return None
        return None

    @staticmethod
    def is_op_sys_type(sys):
        """
        Returns True if the operating system type is sys.
        
        :param sys: Used to determine the operating system type.
        :return: True if the operating system type is equal to sys, and False otherwise.
        """
        op_sys = USys.getOperatingSystemType()
        return op_sys is not None and op_sys[0] == sys

    @staticmethod
    def is_op_sys(sys):
        """
        Returns True if the operating system is sys, and False otherwise.
        
        :param sys: Used to determine which operating system is being used.
        :return: True if the operating system is equal to sys, and False otherwise.
        """
        op_sys = USys.getOperatingSystem()
        return op_sys is not None and op_sys == sys
    
    @staticmethod
    def get_current_file_parent_parent_path(current_script_path):
        """
        Returns the parent of the parent directory of this file.
        
        :param current_script_path: Used to get the path of the current script.
        :return: the parent of the parent of the current script's path.
        """
        parent_parent_path = os.path.normpath(current_script_path + os.sep + os.pardir + os.sep + os.pardir)
        return parent_parent_path

    @staticmethod
    def get_current_file_parent_path(current_script_path):
        """
        Returns the parent path of the current file.
        
        :param current_script_path: Used to get the path of the current script.
        :return: the parent path of the current script.
        """
        parent_path = os.path.normpath(current_script_path + os.sep + os.pardir)
        return parent_path


class UTime(object):

    @staticmethod
    def time_to_string(timeTf, micro=False):
        """
        Converts a time in seconds to a string.
        
        :param timeTf: Used to convert the time in seconds to a string.
        :param micro=False: Used to specify whether the microseconds should be included in the string.
        :return: a string representation of the time passed, if it is not a float then it returns None.
        """
        if UType.is_numeric(timeTf):
            try:
                date_time = datetime.fromtimestamp(timeTf)
                if micro:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S %f')
                else:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S')
                
            except Exception:
                return None
        
        return None

    @staticmethod
    def get_elapsed_time(tim, default=None):
        """
        Returns the elapsed time between two timestamps.
        
        :param tim: Used to pass in the time that is being converted.
        :param default=None: Used to specify a default value to return if the input is not an integer or float.
        :return: the time if it's an integer or float, otherwise it returns default value.
        """
        if UType.is_int(tim) or UType.is_float(tim):
            return time.time()-UType.get_float(tim)
        return default
        
    @staticmethod
    def string_to_time(text, formatF, default=None):
        """
        Converts a string to a time object.
        
        :param text: Used to specify the string to be converted.
        :param formatF: Used to specify the format of the string that is being converted to a time object.
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
    def get_time_search(timeB, timeSearch='23:59:59'):
        """
        Returns the time in seconds from the beginning of epoch based on a given date and time.
        
        :param timeB: Used to pass the time in seconds since epoch.
        :param timeSearch='23:59:59': Used to set the time to 23:59:59, so that all logs from that day are returned.
        :return: the time search given the timeB.
        :doc-author: Trelent
        """
        if UType.is_float(timeB):
            try:
                sTime = time.gmtime(timeB)
                return time.mktime(time.strptime(str(sTime[2])+'-'+str(sTime[1])+'-'+str(sTime[0])+' '+str(timeSearch), "%d-%m-%Y %H:%M:%S"))
            except Exception:
                return None
        return None