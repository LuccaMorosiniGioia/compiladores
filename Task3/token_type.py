from enum import Enum

class Token_type(Enum):
    NUM = 1,
    MINUS = 2,
    PLUS = 3,
    SLASH = 4,
    STAR = 5, 
    EOF = 6,
    INVALID = 7

class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme
        
    def to_string(self):
        return "Token [type=" + self.type.name + ", lexeme=" + str(self.lexeme) + "]"
    

