import tkinter

def loop(n):
    label['text'] = str(n)
    root.after(500, loop, n+1) # call loop(n+1) in 0.5 seconds

root = tkinter.Tk()
label = tkinter.Label(font=(None, 100))
label.pack()
root.after_idle(loop, 0)  # start loop
root.after(5000, root.destroy)  # quit in 5 seconds
# center window
#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.mainloop()