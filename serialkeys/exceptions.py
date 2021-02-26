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

# 510 Only a positive count of keys can be generated
# 520 The key must have at least 4 digits
# 530 Only positive chunk-length is allowed
# 550 Alphabet must contain at least of 4 different tokens
# 560 Too many keys requested for digit count and alphabet



class Custom_Exception(Exception):
    """Template for custom excelptions"""
    def __init__(self):
        self.message = ''  
        self.code = 0
    def __str__(self):
        return str(self.message) 


class Exception_OnlyPositiveCount(Custom_Exception):
    """Negative count of keys requested"""
    def __init__(self):
        self.message ='Only a positive count of keys can be generated'  
        self.code = 510
        
        
class Exception_KeyTooShort(Custom_Exception):
    """The key is too short"""
    def __init__(self):
        self.message ='The key must have at least 4 digits'  
        self.code = 520       


class Exception_ChunkLenghtNotPositive(Custom_Exception):
    """Chunks must have >1 length"""
    def __init__(self):
        self.message ='Only positive chunk-length is allowed'  
        self.code = 530  
        

class Exception_AlphabetTooSmall(Custom_Exception):
    """Alphabet too small"""
    def __init__(self):
        self.message ='Alphabet must contain at least of 4 different tokens'  
        self.code = 550  


class Exception_TooManyKeysRequested(Custom_Exception):
    """Too many keys for digit count and alphabet"""
    def __init__(self):
        self.message ='Too many keys requested for digit count and alphabet'  
        self.code = 560 

       
