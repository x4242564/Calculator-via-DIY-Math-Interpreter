from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

def calculate(text):
    try:
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        print(f"Tokens: {list(tokens)}")
        parser = Parser(tokens)
        tree = parser.parse()
        print(f"Parsed tree: {tree}")
        if not tree: calculate(text)
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(f"Result: {value}")
        if value.is_integer():
            value.int()  # Removes decimal point if the value is an integer
        return value
    except Exception as e:
        print(f"Error: {e}")
        return None
        