import tkinter as tk
win = tk.Tk()
menubar = tk.Menu(win)
win.config(menu=menubar)
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label='About/ How to use')
settings_menu.add_command(label='Exit')
menubar.add_cascade(label='Settings', menu=settings_menu)

text = tk.Text(win, width=100, height=40, bg="white", wrap='word')
text.pack(side='left')

win2 = tk.Tk()

win.mainloop()