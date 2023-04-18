from token_type import *

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
        


    
    def get_type(self, op):
        if op == '-': return Token_type.MINUS
        elif op == '+': return Token_type.PLUS
        elif op == '/': return Token_type.SLASH
        elif op == '*': return Token_type.STAR    
        elif op == '': return Token_type.EOF
        else: return -1
    
    def get_num(self, num):
        if str(num).isnumeric():
            return Token_type.NUM
        return -1
    
    def get_token(self, token):
        token_type = self.get_num(token)
        if token_type != -1:
            return Token(token_type, int(token))
        
        token_type = self.get_type(token)
        if token_type != -1:
            return Token(token_type, token)
        
        if token == '': return Token(Token_type.EOF, token)

        return Token(Token_type.INVALID, token)