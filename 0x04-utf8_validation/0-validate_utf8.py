#!/usr/bin/python3
"""
module 0-validate_utf8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List[int] - a list of integers representing bytes of data
    :return: bool - True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Get the eight least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            # UTF-8 character can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For the remaining bytes in the UTF-8
            # character, they must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
