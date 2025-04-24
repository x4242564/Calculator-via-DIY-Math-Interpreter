from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    POWER = 5
    LPAREN = 6
    RPAREN = 7

@dataclass
class Token:
    '''Data class that holds numerical values or operator types'''
    type: TokenType
    value: any = None # None is default value if the token type does not hold one

    def __repr__(self):
        '''Formats tokens name and value if applicable'''
        return self.type.name + (f':{self.value}' if self.value != None else '')