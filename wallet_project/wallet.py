import tkinter as tk
win = tk.Tk()

def on_click(event):
    button_text = event.widget.cget('text')
    print(button_text)

button = tk.Button(win, text='Hello')
button.pack()
button2 = tk.Button(win, text='World')
button2.pack()
button.bind('<Button-1>', on_click)
button2.bind('<Button-1>', on_click)

win.mainloop()