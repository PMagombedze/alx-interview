#!/usr/bin/python3


"""
utf validation
"""


def validUTF8(data):
    """valid utf8"""
    for x in data:
        if x > 127 or x < 0:
            return False
    return True
