#!/usr/bin/python3


"""
utf validation
"""


def validUTF8(data):
    """valid utf8"""
    count = 0
    for x in data:
        BIT = format(x, '#010b')[-8:]
        if count == 0:
            for bit in BIT:
                if bit == '0':
                    break
                count += 1
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (BIT[0] == '1' and BIT[1] == '0'):
                return False
        count -= 1
    return count == 0
