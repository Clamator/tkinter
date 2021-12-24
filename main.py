import tkinter as tk
from funcs import print_text_in_console


def add_label():
    label = tk.Label(win, text='text')
    label.pack()  # размещает текст непосредственно в окне

count = 0
def counter():
    global count
    count += 1
    counter_func['text'] = f'counter: {count}'

def disable_button_func():
    if count % 2 == 0:
         print('smth enabled')
    else:
        print('smth disabled')



win = tk.Tk()
win.title('headhunter searcher')
win.geometry('1000x600+500+300')
# win.resizable(False, False)

# window icon change
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)

hello_button = tk.Button(win, text='Hello!',
                         command=print_text_in_console,
                         )
print_text_in_tab = tk.Button(
    win, text='print text in tab',
    command=add_label,
)

new_lambda = tk.Button(win, text='new lambda',
                       command=lambda: tk.Label(win, text='lambda text').pack())

counter_func = tk.Button(win, text=f'counter: {count}',
                         command=counter,
                         bg='red',
                         activebackground='green')

disable_button = tk.Button(win, text='disable button',
                           bg='yellow',
                           activebackground='red',
                           command=disable_button_func)


hello_button.pack()
print_text_in_tab.pack()
new_lambda.pack()
counter_func.pack()
disable_button.pack()

win.mainloop()
