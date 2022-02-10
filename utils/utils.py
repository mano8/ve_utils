#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

class UType(object):
    @staticmethod
    def isStr(s):
        """ Test if value is string type """
        return (type(s) is str)

    @staticmethod
    def isBool(s):
        """ Test if value is Bool type """
        return (type(s) is bool)
    
    @staticmethod
    def isInt(s):
        """ Test if value is Int type """
        return (type(s) is int)
    
    @staticmethod
    def isFloat(s):
        """ Test if value is Float type """
        return (type(s) is float)
    
    @staticmethod
    def isNumeric(s):
        """ Test if value is Numeric type """
        if UType.isInt(s) or UType.isFloat(s):
            return True
        return False
    
    @staticmethod
    def isDict(s):
        """ Test if value is Dict type """
        return (type(s) is dict)

    @staticmethod
    def isTuple(s):
        """ Test if value is Tuple type """
        return (type(s) is tuple)

    @staticmethod
    def isList(s):
        """ Test if value is List type """
        return (type(s) is list)

    @staticmethod
    def getInt(nb, default = 0):
        try:
            return int(nb)
        except Exception:
            return default
        return default
    
    @staticmethod
    def getFloat(nb, default = 0.0):
        try:
            return float(nb)
        except Exception:
            return default
        return default
    
    @staticmethod
    def getRoundedFloat(nb, rnd, default = 0.0):
        try:
            nb = UType.getFloat(nb, default)
            rnd = UType.getInt(rnd)
            return round(nb, rnd)
        except Exception:
            return default
        return default
    
    @staticmethod
    def getStr(val, default = None):
        """
        Format value to string.

        Args:
            val : The value to format
            default (optional): If error occurs return default value. Defaults to None.

        Returns:
            str: Return string representation of value or default if any error occurs
        """
        try:
            return str(val)
        except Exception:
            return default
        return default
    
    @staticmethod
    def formatByType(val, data_type, float_round=None):
        """
        Format value to data type format

        Args:
            val: The value to format
            data_type (str): The data type to format value
            float_round (int, optional): When data type is float, value can be rounded from number of decimal places. Value must be (10, 100, 1000, ...). Defaults to None.

        Returns:
            Formatted value
        """
        if data_type == "int":
            return UType.getInt(val)
        elif data_type == "float":
            if float_round is not None:
                return UType.getRoundedFloat(UType.getFloat(val), float_round)
            return UType.getFloat(val)
        elif data_type == "onOff":
            return UType.boolToOnOff(val)
        elif data_type == "intBool":
            return UType.stringToIntBool(val)
        elif data_type == "bool":
            return UType.strToBool(val)
        elif data_type == "str":
            return UType.getStr(val)
        elif data_type == "intString":
            return UType.intToFormattedString(val)
        return val
    
    @staticmethod
    def isValidFormat(val, data_type, default = None):
        """
        Test if value type is valid. If type not reached return default.
        Args:
            val: The value to test
            data_type (str): The data type to test
            default (optional): If type not reached return default. Defaults to None.

        Returns:
            bool: Return True if value data type test success or False. If type not reached return default
        """
        if data_type == "int":
            return UType.isInt(val)
        elif data_type == "float":
            return UType.isFloat(val)
        elif data_type == "str":
            return UType.isStr(val)
        elif data_type == "bool":
            return UType.isBool(UType.strToBool(val))
        elif data_type == "dict":
            return UType.isDict(val)
        elif data_type == "list":
            return UType.isList(val)
        return default
    
    @staticmethod
    def intToFormattedString(nb):
        if UType.isInt(nb):
            if nb < 10 and nb >= 0:
                return "0%s"%(nb)
            return "%s"%(nb)
        return None
    
    @staticmethod
    def strToBool(s, default=False):
        if UType.isBool(s):  # do not convert if already a boolean
            return s
        elif UType.isStr(s):
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
        elif UType.isInt(s):
            return s == 1
        else:
            if UType.isBool(default):  # do not convert if already a boolean
                return default
        return False
    
    @staticmethod
    def boolToIntText(boolT):
        r = UType.strToBool(boolT)
        if boolT:
            return "1"
        return "0"
    
    @staticmethod
    def boolToOnOff(boolT):
        r = UType.strToBool(boolT)
        if boolT:
            return "On"
        return "Off"

    @staticmethod
    def boolToStrState(boolT):
        r = UType.strToBool(boolT)
        if boolT:
            return "Ok"
        return "Error"

    @staticmethod
    def stringToIntBool(text, default=False):
        r = UType.strToBool(text)
        if r == True:
            return 1
        elif r == False:
            return 0
        return default
    
    @staticmethod
    def stringToFloat(text, default=0.0):
        if UType.isStr(text):
            try:
                text = text.replace(',', '.')
                return UType.getFloat(text)
            except Exception:
                return default
        elif UType.isFloat(text):
            return text
        return default
    
    @staticmethod
    def getKeysFromDict(data, list_keys):
        res = dict()
        if UType.isDict(data) and UType.isList(list_keys):

            for key in list_keys:
                if UType.isStr(key) and key in data:
                    res[key] = data.get(key)
        return res


class USys(object):
    
    @staticmethod
    def getOperatingSystem():
        try:
            import sys
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
    def getOperatingSystemType():
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
    def isOpSysType(self, sys):
        """ Test if is sys operating System Type """
        op_sys = USys.getOperatingSystemType()
        return op_sys is not None and op_sys[0] == sys

    @staticmethod
    def isOpSys(self, sys):
        """ Test if is win32 System """
        op_sys = USys.getOperatingSystem()
        return op_sys is not None and op_sys == sys

class UTime(object):

    @staticmethod
    def timeToString(timeTf, micro=False):
        """
            Format Timstamp unix to string
        """
        if UType.isFloat(timeTf):
            try:
                import datetime
                date_time = datetime.fromtimestamp(timeTf)
                if micro:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S %f')
                else:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S')
                
            except Exception:
                return None
        
        return None

    @staticmethod
    def getElapsedTime(tim, default=None):
        """
        Get elapsed time from now
        Args:
            tim (Union[float, int]): The older timestamp
            default (Union[float, int], optional): If invalid older time return default. Defaults to None.

        Returns:
            [float]: Return elapsed time
        """
        if UType.isInt(tim) or UType.isFloat(tim):
            return time.time()-UType.getFloat(tim)
        return default
        
    @staticmethod
    def stringToTime(text, formatF, default=None):
        """
            Format Timstamp unix to string
        """
        if UType.isStr(text) and UType.isStr(formatF):
            try:
                return time.mktime(time.strptime(text, formatF))

            except Exception:
                return default
        return default

    @staticmethod
    def getTimeSearch(timeB, timeSearch='23:59:59'):
        if UType.isFloat(timeB):
            try:
                sTime = time.gmtime(timeB)
                return time.mktime(time.strptime(str(sTime[2])+'-'+str(sTime[1])+'-'+str(sTime[0])+' '+str(timeSearch), "%d-%m-%Y %H:%M:%S"))
            except Exception:
                return None
        return None