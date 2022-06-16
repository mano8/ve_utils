# -*- coding: utf-8 -*-
"""
Time and date helper methods.

Contain only static methods.
"""
import time
from datetime import datetime
from ve_utils.utype import UType

__author__ = "Eli Serra"
__copyright__ = "Copyright 2020, Eli Serra"
__deprecated__ = False
__license__ = "MIT"
__status__ = "Production"
__version__ = "2.0.0"


class UTime:
    """Time Helper methods."""

    @staticmethod
    def get_timestamp_from_datetime(
            date_time: datetime
    ) -> float:
        """Get timestamp from datetime object"""
        if isinstance(date_time, datetime):
            return datetime.timestamp(date_time)
        return None

    @staticmethod
    def get_utc_timestamp(timestamp: int or float) -> float:
        """Get timestamp from datetime object"""
        if UType.is_numeric(timestamp, not_null=True):
            return UTime.get_timestamp_from_datetime(
                datetime.utcfromtimestamp(timestamp)
            )

    @staticmethod
    def time_to_string(
                        timestamp: int or float,
                        micro: bool = False
                        ) -> str or None:
        """
        Convert a time in seconds to a string.

        :param timestamp: Used to convert the time in seconds to a string.
        :param micro:
            Used to specify whether the microseconds
            should be included in the string.
        :return:
            a string representation of the time passed,
            if it is not a float then it returns None.
        """
        if UType.is_numeric(timestamp):
            try:
                date_time = datetime.fromtimestamp(timestamp)
                if micro:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S %f')
                else:
                    return date_time.strftime('%d/%m/%Y %H:%M:%S')

            except Exception:
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
        :param default:
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
            time_format: str,
            default: float or None = None
            ) -> float or None:
        """
        Convert a string to a time object.

        :param text: Used to specify the string to be converted.
        :param time_format:
            Used to specify the format of the string
            that is being converted to a time object.
        :param default: Used to set a default value for the function.
        :return: a time object converted from the given string and format.
        """
        if UType.is_str(text) and UType.is_str(time_format):
            try:
                return time.mktime(time.strptime(text, time_format))

            except Exception:
                return default
        return default

    @staticmethod
    def get_time_search(
            timestamp: int or float,
            time_search: str = '23:59:59'
            ) -> int or float:
        """
        Return formatted time.

        :param timestamp: Used to pass the time in seconds since epoch.
        :param time_search:
            Used to set the time to 23:59:59,
            so that all logs from that day are returned.
        :return: the time search given the timeB.
        :doc-author: Trelent
        """
        if UType.is_float(timestamp):
            try:
                gmt_tuple = time.gmtime(timestamp)
                return time.mktime(
                    time.strptime(
                        "%s-%s-%s %s" % (
                            str(gmt_tuple[2]),
                            str(gmt_tuple[1]),
                            str(gmt_tuple[0]),
                            str(time_search)
                        ),
                        "%d-%m-%Y %H:%M:%S"
                    )
                )
            except Exception:
                return None
        return None
