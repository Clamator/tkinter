import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = main_window.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    main_window.delete(0, tk.END)
    main_window.insert(0, value + str(digit))


def add_operation(operation):
    value = main_window.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = main_window.get()
    main_window.delete(0, tk.END)
    main_window.insert(0, value + operation)


def calculate():
    value = main_window.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    main_window.delete(0, tk.END)
    try:
        main_window.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showerror('Attention', 'You should insert numbers only')
        main_window.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showerror('Attention', 'Division by zero')
        main_window.insert(0, '0')


def do_clear():
    main_window.delete(0, tk.END)
    main_window.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(win, text=digit, bg='white', bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(win, text=operation, bg='white', bd=5, font=('Arial', 15),
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(win, text=operation, bg='white', bd=5, font=('Arial', 15),
                     command=calculate)


def make_clear_button(digit):
    return tk.Button(win, text=digit, bg='white', bd=5, font=('Arial', 15), command=lambda: do_clear())


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '-+*/':
        add_operation(event.char)
    elif event.char in '\r=':
        calculate()


win = tk.Tk()
win.geometry('345x257+750+300')
win['bg'] = 'black'
win.title('Calculator')
win.bind('<Key>', press_key)

main_window = tk.Entry(win, bd=5, justify=tk.RIGHT, font=('Arial', 15), width=15)
main_window.insert(0, '0')
main_window.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

make_digit_button(1).grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize='100')
win.grid_columnconfigure(1, minsize='100')
win.grid_columnconfigure(2, minsize='100')

win.grid_rowconfigure(1, minsize='50')
win.grid_rowconfigure(2, minsize='50')
win.grid_rowconfigure(3, minsize='50')
win.grid_rowconfigure(4, minsize='50')

win.mainloop()
