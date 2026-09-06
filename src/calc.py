import customtkinter as ctk
import argparse

from main import calculate
import logger
from logger import log, verbose_log

ap = argparse.ArgumentParser()

ap.add_argument("--debug", "--d", action = "store_true", help="Sets debug mode (optional)")

args = ap.parse_args()

log(f"Debug mode: {args.debug}")
verbose_log(f"Verbose logging: {logger.verbose}")


calculation = ''
eval = ''
ans = ''

class DebugMenu(ctk.CTkScrollableFrame):
    def __init__(self, master, title):
        super().__init__(master, label_text = title)
        self.grid_columnconfigure(0, weight=1)

        self.btn_dim = ctk.CTkButton(self, text = 'Fetch Window Size', command = master.get_window_size, font = ('Ariel', 14))
        self.btn_dim.grid(row = 0, column = 0, columnspan = 1, padx = 4, pady = 4)

        self.v_var = ctk.IntVar(value = int(logger.verbose))
        self.v_log = ctk.CTkCheckBox(self, command = self.toggle_verbose, variable = self.v_var, text="Verbose Logging")
        self.v_log.grid(row = 1, column=0, padx = 4, pady = 4)

    def toggle_verbose(self):
        logger.verbose = (self.v_var.get()) == 1

        log(f"Verbose logging: {logger.verbose}")

class Calculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(list(range(0,4)), weight=1)
        btn_width = 75

        self.result_txt = ctk.CTkTextbox(self, state = "disabled", height = 2, font = ('Arial', 24), wrap = "none")
        self.result_txt.grid(row = 0, column = 0, columnspan = 5, sticky = "ew", padx = 6, pady = 4)

        self.btn_7 = ctk.CTkButton(self, text = '7', command = lambda: self.add_to_calc(7), font = ('Ariel', 14), width = btn_width)
        self.btn_7.grid(row = 2, column = 0, sticky = "ew", padx = 6, pady = 4)
        self.btn_8 = ctk.CTkButton(self, text = '8', command = lambda: self.add_to_calc(8), font = ('Ariel', 14), width = btn_width)
        self.btn_8.grid(row = 2, column = 1, sticky = "ew", padx = 6, pady = 4)
        self.btn_9 = ctk.CTkButton(self, text = '9', command = lambda: self.add_to_calc(9), font = ('Ariel', 14), width = btn_width)
        self.btn_9.grid(row = 2, column = 2, sticky = "ew", padx = 6, pady = 4)

        self.btn_4 = ctk.CTkButton(self, text = '4', command = lambda: self.add_to_calc(4), font = ('Ariel', 14), width = btn_width)
        self.btn_4.grid(row = 3, column = 0, sticky = "ew", padx = 6, pady = 4)
        self.btn_5 = ctk.CTkButton(self, text = '5', command = lambda: self.add_to_calc(5), font = ('Ariel', 14), width = btn_width)
        self.btn_5.grid(row = 3, column = 1, sticky = "ew", padx = 6, pady = 4)
        self.btn_6 = ctk.CTkButton(self, text = '6', command = lambda: self.add_to_calc(6), font = ('Ariel', 14), width = btn_width)
        self.btn_6.grid(row = 3, column = 2, sticky = "ew", padx = 6, pady = 4)

        self.btn_1 = ctk.CTkButton(self, text = '1', command = lambda: self.add_to_calc(1), font = ('Ariel', 14), width = btn_width)
        self.btn_1.grid(row = 4, column = 0, sticky = "ew", padx = 6, pady = 4)
        self.btn_2 = ctk.CTkButton(self, text = '2', command = lambda: self.add_to_calc(2), font = ('Ariel', 14), width = btn_width)
        self.btn_2.grid(row = 4, column = 1, sticky = "ew", padx = 6, pady = 4)
        self.btn_3 = ctk.CTkButton(self, text = '3', command = lambda: self.add_to_calc(3), font = ('Ariel', 14), width = btn_width)
        self.btn_3.grid(row = 4, column = 2, sticky = "ew", padx = 6, pady = 4)

        self.btn_0 = ctk.CTkButton(self, text = '0', command = lambda: self.add_to_calc(0), font = ('Ariel', 14), width = btn_width)
        self.btn_0.grid(row = 5, column = 1, sticky = "ew", padx = 6, pady = 4)
        self.btn_lparen = ctk.CTkButton(self, text = '(', command = lambda: self.add_to_calc('('), font = ('Ariel', 14), width = btn_width)
        self.btn_lparen.grid(row = 5, column = 0, sticky = "ew", padx = 6, pady = 4)
        self.btn_rparen = ctk.CTkButton(self, text = ')', command = lambda: self.add_to_calc(')'), font = ('Ariel', 14), width = btn_width)
        self.btn_rparen.grid(row = 5, column = 2, sticky = "ew", padx = 6, pady = 4)

        self.btn_plus = ctk.CTkButton(self, text = '+', command = lambda: self.add_to_calc('+'), font = ('Ariel', 14), width = btn_width)
        self.btn_plus.grid(row = 5, column = 3, sticky = "ew", padx = 6, pady = 4)
        self.btn_minus = ctk.CTkButton(self, text = '-', command = lambda: self.add_to_calc('-'), font = ('Ariel', 14), width = btn_width)
        self.btn_minus.grid(row = 4, column = 3, sticky = "ew", padx = 6, pady = 4)
        self.btn_multiply = ctk.CTkButton(self, text = '*', command = lambda: self.add_to_calc('*'), font = ('Ariel', 14), width = btn_width)
        self.btn_multiply.grid(row = 3, column = 3, sticky = "ew", padx = 6, pady = 4)
        self.btn_divide = ctk.CTkButton(self, text = '/', command = lambda: self.add_to_calc('/'), font = ('Ariel', 14), width = btn_width)
        self.btn_divide.grid(row = 2, column = 3, sticky = "ew", padx = 6, pady = 4)
        self.btn_power = ctk.CTkButton(self, text = '^', command = lambda: self.add_to_calc('^'), font = ('Ariel', 14), width = btn_width)
        self.btn_power.grid(row = 1, column = 3, sticky = "ew", padx = 6, pady = 4)

        self.btn_point = ctk.CTkButton(self, text = '.', command = lambda: self.add_to_calc('.'), font = ('Ariel', 14), width = btn_width)
        self.btn_point.grid(row = 6, column = 1, sticky = "ew", padx = 6, pady = 4)
        self.btn_ans = ctk.CTkButton(self, text = 'Ans', command = lambda: self.add_to_calc(ans), font = ('Ariel', 14), width = btn_width)
        self.btn_ans.grid(row = 6, column = 2, sticky = "ew", padx = 6, pady = 4)
        self.btn_eval = ctk.CTkButton(self, text = '=', command = self.evaluate_calc, font = ('Ariel', 14), width = btn_width)
        self.btn_eval.grid(row = 6, column = 3, sticky = "ew", padx = 6, pady = 4)
        self.btn_clear = ctk.CTkButton(self, text = 'C', command = self.clear, font = ('Ariel', 14), width = btn_width)
        self.btn_clear.grid(row = 6, column = 0, sticky = "ew", padx = 6, pady = 4)
        self.btn_backspace = ctk.CTkButton(self, text = 'Del', command = self.backspace, font = ('Ariel', 14), width = btn_width)
        self.btn_backspace.grid(row = 1, column = 0, sticky = "ew", padx = 6, pady = 4)

    def delete(self):
        self.result_txt.configure(state = "normal")
        self.result_txt.delete(1.0, 'end')
        self.result_txt.configure(state = "disabled")

    def insert(self, text):
        self.result_txt.configure(state = "normal")
        self.result_txt.insert(1.0, text)
        self.result_txt.configure(state = "disabled")

    def add_to_calc(self, char: str | int):
        '''Adds the given character to the calculation string.'''
        global calculation
        global eval
        if eval != '':
            self.clear()
        calculation += str(char)
        self.delete()
        self.insert(calculation)

    def evaluate_calc(self):
        '''Evaluates the current calculation and displays the result.'''
        global eval
        eval = str(calculate(calculation))
        print(f'{calculation} = {eval}')
        if eval == "None":
            self.display_error()
        else:
            self.delete()
            self.insert(eval)

    def clear(self):
        '''Clears the calculation and result display. Saves the last result in 'ans' if available.'''
        global calculation
        global eval
        global ans
        calculation = ''
        if eval != '':
            ans = eval
            eval = ''
        self.delete()

    def backspace(self):
        '''Removes the last character from the calculation string.'''
        global calculation
        global ans
        global eval
        if eval != '': # check if the last operation was an evaluation, if so, reset eval and ans
            ans = ''
            eval = ''
        else:
            calculation = calculation[:-1]
        self.delete()
        self.insert(calculation)

    def display_error(self):
        '''Displays an error message in the result text widget.'''
        self.delete()
        self.insert('Error')
        
class App(ctk.CTk):

    def __init__(self, debug):
        super().__init__()

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        self.title('DIY Calculator')

        if debug:
            self.minsize(500,290)
            self.geometry("500x290")
        else:
            self.minsize(265,290)
            self.geometry("265x290")

        self.grid_columnconfigure([0,1], weight = 1)

        self.calculator_frame = Calculator(self)
        self.calculator_frame.grid(row = 0, column = 0)

        if debug:
            self.debug_menu_frame = DebugMenu(self, title = "Menu")
            self.debug_menu_frame.grid(row = 0, column = 1, padx=10)

    def get_window_size(self):
        width = self._current_width
        height = self._current_height

        log(f"Window dimensions: {width}, {height}")
        

if __name__ == "__main__":
    app = App(args.debug)
    app.mainloop()