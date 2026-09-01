from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

def calculate(text):
    try:
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: calculate(text)
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        if value.is_integer():
            value = value.int()  # Removes decimal point if the value is an integer
        print(f"Result: {value}")
        return value
    except Exception as e:
        print(e)
