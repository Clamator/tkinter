import tkinter as tk


def add_digit(digit):
    value = main_window.get() + str(digit)
    main_window.delete(0, tk.END)
    main_window.insert(0, value)


def make_digit_button(digit):
    return tk.Button(win, text=digit, bg='white', bd=5, font=('Arial', 15), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(win, text=operation, bg='white', bd=5, font=('Arial', 15), command=lambda: add_digit(operation))


win = tk.Tk()
win.geometry('400x500+750+300')
win['bg'] = 'yellow'
win.title('Calculator')

main_window = tk.Entry(win, bd=5, justify=tk.RIGHT, font=('Arial', 15), width=15)
main_window.grid(row=0, column=0, columnspan=3, stick='we')

make_digit_button(1).grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, columnspan=2, stick='wens', padx=5, pady=5)

make_digit_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_digit_button('_').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_digit_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_digit_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)




win.grid_columnconfigure(0, minsize='100')
win.grid_columnconfigure(1, minsize='100')
win.grid_columnconfigure(2, minsize='100')

win.grid_rowconfigure(1, minsize='50')
win.grid_rowconfigure(2, minsize='50')
win.grid_rowconfigure(3, minsize='50')
win.grid_rowconfigure(4, minsize='50')

win.mainloop()
