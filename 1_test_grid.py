import tkinter as tk

win = tk.Tk()
win.title('testing grid')
win.geometry('600x600')

for i in range(4):
    for j in range(2):
        tk.Button(win, text=f'button {i}x{j}').grid(row=i, column=j, stick='we')

win.grid_columnconfigure(0, minsize='100')
win.grid_columnconfigure(1, minsize='150')

tk.mainloop()
