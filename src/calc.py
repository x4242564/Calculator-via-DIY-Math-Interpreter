import tkinter as tk
from main import calculate

calculation = ''
eval = ''
ans = ''

def add_to_calc(char: str | int):
    '''Adds the given character to the calculation string.'''
    global calculation
    global eval
    if eval != '':
        clear()
    calculation += str(char)
    result_txt.delete(1.0, 'end')
    result_txt.insert(1.0, calculation)

def evaluate_calc():
    '''Evaluates the current calculation and displays the result.'''
    global eval
    eval = str(calculate(calculation))
    print(f'{calculation} = {eval}')
    if eval == "None":
        display_error()
    else:
        result_txt.delete(1.0, 'end')
        result_txt.insert(1.0, eval)

def clear():
    '''Clears the calculation and result display. Saves the last result in 'ans' if available.'''
    global calculation
    global eval
    global ans
    calculation = ''
    if eval != '':
        ans = eval
        eval = ''
    result_txt.delete(1.0, 'end')

def backspace():
    '''Removes the last character from the calculation string.'''
    global calculation
    global ans
    global eval
    if eval != '': # check if the last operation was an evaluation, if so, reset eval and ans
        ans = ''
        eval = ''
    else:
        calculation = calculation[:-1]
    result_txt.delete(1.0, 'end')
    result_txt.insert(1.0, calculation)

def display_error():
    '''Displays an error message in the result text widget.'''
    result_txt.delete(1.0, 'end')
    result_txt.insert(1.0, 'Error')

root = tk.Tk()
root.title('DIY Calculator')
root.geometry('300x330')

result_txt = tk.Text(root, height = 2, width = 16, font = ('Arial', 24))
result_txt.grid(columnspan = 5)

btn_7 = tk.Button(root, text = '7', command = lambda: add_to_calc(7), width = 4, font = ('Ariel', 14))
btn_7.grid(row = 2, column = 1)
btn_8 = tk.Button(root, text = '8', command = lambda: add_to_calc(8), width = 4, font = ('Ariel', 14))
btn_8.grid(row = 2, column = 2)
btn_9 = tk.Button(root, text = '9', command = lambda: add_to_calc(9), width = 4, font = ('Ariel', 14))
btn_9.grid(row = 2, column = 3)

btn_4 = tk.Button(root, text = '4', command = lambda: add_to_calc(4), width = 4, font = ('Ariel', 14))
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(root, text = '5', command = lambda: add_to_calc(5), width = 4, font = ('Ariel', 14))
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(root, text = '6', command = lambda: add_to_calc(6), width = 4, font = ('Ariel', 14))
btn_6.grid(row = 3, column = 3)

btn_1 = tk.Button(root, text = '1', command = lambda: add_to_calc(1), width = 4, font = ('Ariel', 14))
btn_1.grid(row = 4, column = 1)
btn_2 = tk.Button(root, text = '2', command = lambda: add_to_calc(2), width = 4, font = ('Ariel', 14))
btn_2.grid(row = 4, column = 2)
btn_3 = tk.Button(root, text = '3', command = lambda: add_to_calc(3), width = 4, font = ('Ariel', 14))
btn_3.grid(row = 4, column = 3)

btn_0 = tk.Button(root, text = '0', command = lambda: add_to_calc(0), width = 4, font = ('Ariel', 14))
btn_0.grid(row = 5, column = 2)
btn_lparen = tk.Button(root, text = '(', command = lambda: add_to_calc('('), width = 4, font = ('Ariel', 14))
btn_lparen.grid(row = 5, column = 1)
btn_rparen = tk.Button(root, text = ')', command = lambda: add_to_calc(')'), width = 4, font = ('Ariel', 14))
btn_rparen.grid(row = 5, column = 3)

btn_plus = tk.Button(root, text = '+', command = lambda: add_to_calc('+'), width = 4, font = ('Ariel', 14))
btn_plus.grid(row = 5, column = 4)
btn_minus = tk.Button(root, text = '-', command = lambda: add_to_calc('-'), width = 4, font = ('Ariel', 14))
btn_minus.grid(row = 4, column = 4)
btn_multiply = tk.Button(root, text = '*', command = lambda: add_to_calc('*'), width = 4, font = ('Ariel', 14))
btn_multiply.grid(row = 3, column = 4)
btn_divide = tk.Button(root, text = '/', command = lambda: add_to_calc('/'), width = 4, font = ('Ariel', 14))
btn_divide.grid(row = 2, column = 4)
btn_power = tk.Button(root, text = '^', command = lambda: add_to_calc('^'), width = 4, font = ('Ariel', 14))
btn_power.grid(row = 1, column = 4)

btn_point = tk.Button(root, text = '.', command = lambda: add_to_calc('.'), width = 4, font = ('Ariel', 14))
btn_point.grid(row = 6, column = 2)
btn_ans = tk.Button(root, text = 'Ans', command = lambda: add_to_calc(ans), width = 4, font = ('Ariel', 14))
btn_ans.grid(row = 6, column = 3)
btn_eval = tk.Button(root, text = '=', command = evaluate_calc, width = 4, font = ('Ariel', 14))
btn_eval.grid(row = 6, column = 4)
btn_clear = tk.Button(root, text = 'C', command = clear, width = 4, font = ('Ariel', 14))
btn_clear.grid(row = 6, column = 1)
btn_backspace = tk.Button(root, text = 'Del', command = backspace, width = 4, font = ('Ariel', 14))
btn_backspace.grid(row = 1, column = 1)

root.mainloop()
