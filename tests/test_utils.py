import unittest
import time
from utils import UType as U, UTime as Utime, USys as Usys

class TestUtils(unittest.TestCase):

    def test_isStr(self):
        """"""
        self.assertTrue(U.isStr("hello"))
        self.assertTrue(U.isStr(""))
        self.assertFalse(U.isStr(0))
        self.assertFalse(U.isStr(True))
        self.assertFalse(U.isStr({}))
        self.assertFalse(U.isStr([]))
    
    def test_isBool(self):
        """"""
        self.assertFalse(U.isBool("hello"))
        self.assertFalse(U.isBool(0))
        self.assertTrue(U.isBool(True))
        self.assertTrue(U.isBool(False))
        self.assertFalse(U.isBool([]))
    
    def test_isInt(self):
        """"""
        self.assertFalse(U.isInt("hello"))
        self.assertTrue(U.isInt(0))
        self.assertFalse(U.isInt(1.2))
        self.assertTrue(U.isInt(0x235))
        self.assertFalse(U.isInt(True))
        self.assertFalse(U.isInt([]))

    def test_isFloat(self):
        """"""
        self.assertFalse(U.isFloat("hello"))
        self.assertTrue(U.isFloat(0.1))
        self.assertFalse(U.isFloat(0))
        self.assertFalse(U.isFloat(True))
        self.assertFalse(U.isFloat([]))

    def test_isNumeric(self):
        """"""
        self.assertFalse(U.isNumeric("hello"))
        self.assertTrue(U.isNumeric(0.1))
        self.assertTrue(U.isNumeric(0))
        self.assertFalse(U.isNumeric(True))
        self.assertFalse(U.isNumeric([]))
    
    def test_isDict(self):
        """"""
        self.assertFalse(U.isDict("hello"))
        self.assertFalse(U.isDict(0.1))
        self.assertFalse(U.isDict(0))
        self.assertFalse(U.isDict(True))
        self.assertFalse(U.isDict([]))
        self.assertTrue(U.isDict({}))
    
    def test_isTuple(self):
        """"""
        self.assertFalse(U.isTuple("hello"))
        self.assertFalse(U.isTuple(0.1))
        self.assertFalse(U.isTuple(0))
        self.assertFalse(U.isTuple(True))
        self.assertFalse(U.isTuple([]))
        self.assertTrue(U.isTuple((0,1)))
        self.assertFalse(U.isTuple({}))

    def test_isList(self):
        """"""
        self.assertFalse(U.isList("hello"))
        self.assertFalse(U.isList(0.1))
        self.assertFalse(U.isList(0))
        self.assertFalse(U.isList(True))
        self.assertTrue(U.isList([]))
        self.assertFalse(U.isList((0,1)))
        self.assertFalse(U.isList({}))
    
    def test_getInt(self):
        """"""
        self.assertTrue(U.getInt("hello", 0) == 0)
        self.assertTrue(U.getInt(0.1) == 0)
        self.assertTrue(U.getInt("bg", 2) == 2)
        self.assertTrue(U.getInt(True) == 1)
        self.assertTrue(U.getInt([]) == 0)

    def test_getFloat(self):
        """"""
        self.assertTrue(U.getFloat("hello", 0.0) == 0.0)
        self.assertTrue(U.getFloat(0.1) == 0.1)
        self.assertTrue(U.getFloat("bg", 2.5) == 2.5)
        self.assertTrue(U.getFloat(True) == 1.0)
        self.assertTrue(U.getFloat([]) == 0.0)

    def test_getRoundedFloat(self):
        """"""
        self.assertTrue(U.getRoundedFloat("hello", 1, 0.156) == 0.1)
        self.assertTrue(U.getRoundedFloat(0.1665616, 3) == 0.166)
        self.assertTrue(U.getRoundedFloat("bg", 2, 2.589898) == 2.58)

    def test_getStr(self):
        """"""
        self.assertTrue(U.getStr("hello") == "hello")
        self.assertTrue(U.getStr(0.1665616, "world", True) == "world")
        self.assertTrue(U.getStr(10, "by") == "10")
    
    def test_formatByType(self):
        """"""
        self.assertTrue(U.formatByType(32, 'str') == '32')
        self.assertTrue(U.formatByType(True, 'onOff') == 'On')
        self.assertTrue(U.formatByType(False, 'onOff') == 'Off')
        self.assertTrue(U.formatByType(True, 'intBool') == 1)
        self.assertTrue(U.formatByType(False, 'intBool') == 0)
        self.assertTrue(U.formatByType(1.25698789, 'float', 3) == 1.256)
        self.assertTrue(U.formatByType(8, 'intString') == "08")
        self.assertTrue(U.formatByType(10, 'intString') == "10")

    def test_stringToFloat(self):
        """"""
        self.assertTrue(U.stringToFloat('0,125') == 0.125)
        self.assertTrue(U.stringToFloat('0.125') == 0.125)

    def test_strToBool(self):
        """"""
        self.assertTrue(U.strToBool("true"))
        self.assertTrue(U.strToBool("1"))
        self.assertTrue(U.strToBool("On"))
        self.assertTrue(U.strToBool("Ok"))
        self.assertTrue(U.strToBool(1))
        self.assertTrue(U.strToBool(True))
        self.assertFalse(U.strToBool("False"))
        self.assertFalse(U.strToBool("0"))
        self.assertFalse(U.strToBool("Off"))
        self.assertFalse(U.strToBool("Error"))
        self.assertFalse(U.strToBool(0))
        self.assertFalse(U.strToBool(False))

    def test_getElapsedTime(self):
        """"""
        self.assertTrue(Utime.getElapsedTime(32) <= U.getInt(time.time()+32))
    
    def test_timeToString(self):
        """"""
        self.assertTrue(Utime.timeToString(1630193115.6428988) == '29/08/2021 01:25:15')
        self.assertTrue(Utime.timeToString(1630193115.6428988, True) == '29/08/2021 01:25:15 642899')

    def test_stringToTime(self):
        """"""
        self.assertTrue(Utime.stringToTime('29/08/2021', '%d/%m/%Y') == 1630188000.0)
    
    def test_getTimeSearch(self):
        """"""
        self.assertTrue(Utime.getTimeSearch(1630188000.0, '10:12:58') == 1630138378.0)
    
    def test_getOperatingSystem(self):
        """"""
        self.assertTrue(U.isStr(Usys.getOperatingSystem()))
    
    def test_getOperatingSystemType(self):
        """"""
        self.assertTrue(U.isTuple(Usys.getOperatingSystemType()))

if __name__ == '__main__':
    
    unittest.main()