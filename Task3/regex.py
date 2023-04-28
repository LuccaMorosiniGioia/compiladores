from re import compile

class Regex:

    @staticmethod
    def isNum(num):
        regex = compile(r'^-?\d+(?:\.\d*)?$')
        result = regex.match(num)
        return result is not None

    @staticmethod
    def isOp(op):
        regex = compile(r'^[+\-*\/]$')
        result = regex.match(op)

        return result is not None