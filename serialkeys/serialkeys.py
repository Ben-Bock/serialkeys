"""
# -*- coding: utf-8 -*-
#  Serialkeys
#  ---------------
#  A generator for unique serial keys
#
#  Author:  Ben Bock (benbock@live.de)
#  Website: https://github.com/Ben-Bock/serialkeys
#  License: MIT (see LICENSE file)
"""

import math
import secrets
from .exceptions import Exception_OnlyPositiveCount
from .exceptions import Exception_AlphabetTooSmall
from .exceptions import Exception_ChunkLenghtNotPositive
from .exceptions import Exception_KeyTooShort
from .exceptions import Exception_TooManyKeysRequested

DEFAULTALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Serialkeys:
    """A class to generate unique serial keys of given length"""

    def __init__(self, digits: int = 8, _chunksize: int = 4, _delimeter: str = "-", _alphabet: str = DEFAULTALPHABET):
        """Initalizes variables"""

        self.digits = digits
        self.chunksize = _chunksize
        self.delimeter = _delimeter
        self.alphabet = _alphabet

    def chunkString(self, _string: str, _chunksize: int):
        """Creates a list of parts of a given string by a given chunksize"""

        if _chunksize is None:
            _chunksize = self.chunksize
        return list(_string[0+i:_chunksize+i] for i in range(0, len(_string), _chunksize))

    def createCode(self, digits: int, _chunksize: int, _delimeter: str, _alphabet: str):
        """Generates a single random code for a given size, chunksize, delimeters and alphabet"""

        if not digits:
            digits = self.size
        if not _chunksize:
            _chunksize = self.chunksize
        if not _delimeter:
            _delimeter = self.delimeter
        if not _alphabet:
            _alphabet = self.alphabet
        randcode = ''.join(secrets.choice(_alphabet) for _ in range(digits))
        if _chunksize == 1:
            return randcode
        else:
            chunks = self.chunkString(randcode, _chunksize)
            retval = ""
            for chunk in chunks[:-1]:
                retval = retval + chunk + _delimeter
            retval = retval + chunks[-1]
            return retval

    def generate(self, _cnt: int):
        """Generates a list with _cnt distinct codes"""

        if _cnt < 1:           
            raise Exception_OnlyPositiveCount()
        if self.digits < 4:
            raise Exception_KeyTooShort()
        if self.chunksize < 1:
            raise Exception_ChunkLenghtNotPositive
        if len(self.alphabet) < 8:
            raise Exception_AlphabetTooSmall
        if math.factorial(len(self.alphabet)) <= round(math.factorial(self.digits)*_cnt):
            raise Exception_TooManyKeysRequested
        if math.factorial(len(self.alphabet)) <= round(_cnt*self.digits):
            raise Exception_TooManyKeysRequested
        else:
            retval = set()
            counter = 1
            for _ in range(_cnt):
                retval.add(self.createCode(self.digits, self.chunksize, self.delimeter, self.alphabet))
            while len(retval) < _cnt and counter < _cnt:
                retval.add(self.createCode(self.digits, self.chunksize, self.delimeter, self.alphabet))
                counter = counter + 1
            return list(retval)
