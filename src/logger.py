import logging
import os
import sys

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(tag)s] %(message)s")

terminal_handler = logging.StreamHandler(sys.stdout)
terminal_handler.setFormatter(formatter)

file_handler = logging.FileHandler("app_terminal.log")
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)

isLogging = True
isVerbose = True

ansi = {
    "RED" : "\033[31m",
    "GREEN" : "\033[32m",
    "YELLOW" : "\033[33m",
    "BLUE" : "\033[34m",
    "RESET" : "\033[0m" # resets color to default
}

color = {
    "main.py" : ansi["RED"],
    "calc.py" : ansi["RED"],
    "lexer.py" : ansi["GREEN"],
    "tokens.py" : ansi["GREEN"],
    "parser_.py" : ansi["YELLOW"],
    "nodes.py" : ansi["YELLOW"],
    "interpreter.py" : ansi["BLUE"],
}


def log(text):
    if isLogging:
        logger.info(text, extra={"tag": "LOG"})

def verbose_log(text):
    if isVerbose and isLogging:
        filename = os.path.basename(sys._getframe(1).f_code.co_filename)
        tag_color = color.get(filename, ansi["RESET"])
        tag = f"-v LOG {tag_color}{filename}{ansi['RESET']}"
        logger.info(text, extra={"tag": tag})

def error_log(text):
    logger.error(text, extra={"tag": f"{ansi['RED']}ERROR{ansi['RESET']}"})
