import inspect
import os

logging = True
verbose = True

def log(text):
    if log:
        frame = inspect.stack()[1]
        filename = os.path.basename(frame.filename)
        print(f"[LOG] {text}")

def verbose_log(text):
    if verbose:
        frame = inspect.stack()[1]
        filename = os.path.basename(frame.filename)
        print(f"[-v LOG {filename}] {text}")
