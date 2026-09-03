from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

from logger import log, verbose_log
import traceback
import os

def calculate(text):
    try:
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        log(f"calculated result: {value}")
        if value.is_integer():
            value.int()  # Removes decimal point if the value is an integer
        return value
    except Exception as e: # catch errors and point to their origin
        tb = e.__traceback__
        while tb.tb_next: # find the frame of origin (inner-most)
            tb = tb.tb_next
        
        frame = tb.tb_frame
        code = frame.f_code
        filename = os.path.basename(code.co_filename)
        line_number = tb.tb_lineno
        function_name = code.co_name
        log(f"{os.path.splitext(filename)[0]} ERROR {e}")
        verbose_log(f"Error origin: {filename} {function_name}() Line: {line_number}")

def main():
    print("-----------Terminal Calculator-----------")
    while True:
        equation = input("enter equation (\"q\" to quit): ")
        if equation == "q": break
        eval = calculate(equation)
        if eval: print(f'{equation} = {eval}\n')

if __name__ == "__main__":
    main()
