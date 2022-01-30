import tkinter as tk

win = tk.Tk()
win.geometry('600x600+600+300')

menubar = tk.Menu(win)
win.config(menu=menubar)
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label='one')
settings_menu.add_command(label='two')
settings_menu.add_command(label='three')
menubar.add_cascade(label='Options', menu=settings_menu)

settings_menu2 = tk.Menu(menubar, tearoff=0)
settings_menu2.add_command(label='four')
settings_menu2.add_command(label='five')
settings_menu2.add_command(label='six')
menubar.add_cascade(label='Options 2', menu=settings_menu2)

settings_menu3 = tk.Menu(menubar, tearoff=0)
settings_menu3.add_command(label='seven')
settings_menu3.add_command(label='eight')
settings_menu3.add_command(label='nine')
menubar.add_cascade(label='Optoins 3', menu=settings_menu3)

win.mainloop()
