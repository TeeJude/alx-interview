#!/usr/bin/python3
"""Module for a method that determines a data set representing a
valid UTF-8 encoding."""


def validUTF8(data):
    """
    Method that defines a UTF-8 encoding.
    Args:
        data (list[int]): an array of characters represented as 1byte int
    Returns:
        (True): if data is a valid UTF-8 encoding
        (False): if data is a not valid UTF-8 encoding
    """
    byte_count = 0
    Dat1 = 1 << 6
    Dat2 = 1 << 7
    for data_point in data:
        Dat3 = 1 << 7
        if byte_count == 0:
            while Dat3 & data_point:
                byte_count += 1
                Dat3 = Dat3 >> 1
            if byte_count == 0:
                continue
            if byte_count == 1 or byte_count > 4:
                return False
        else:
            if not (data_point & Dat2 and not (data_point & Dat1)):
                return False
        byte_count -= 1
    return not byte_count
