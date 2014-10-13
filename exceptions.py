# coding=utf8

'''
all exceptions
'''


class ExtractException(Exception):
    pass


class NotIncludedError(ExtractException):
    def __init__(self, o_datetime):
        self.code = 30001
        self.message = "%s Not Included"
