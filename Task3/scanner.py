from token_type import *
from regex import Regex

class Scanner:
    def __init__(self):
        self.stack = []

    def scan(self, input):
        for x in input:
            token = self.get_token(x)
            if token.type == Token_type.INVALID:
                print('Error: Unexpected character: ' + str(token.lexeme))
                return None
            else:
                print(token.to_string())
                self.stack.append(token)

        return self.stack
    
    def get_token_type(self, token):
        if Regex.isNum(token): return Token_type.NUM
        if Regex.isOp(token):
            if token == '-': return Token_type.MINUS
            if token == '+': return Token_type.PLUS
            if token == '/': return Token_type.SLASH
            if token == '*': return Token_type.STAR
        if token == '': return Token_type.EOF
        return Token_type.INVALID
    
    def get_token(self, token):
        token_type = self.get_token_type(token)
        if(token_type == Token_type.NUM):
            return Token(token_type, float(token))
        else:
            return Token(token_type, token)