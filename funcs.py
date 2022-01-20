import tkinter as tk
win = tk.Tk()
win.geometry('400x480+600+300')
# win.attributes('-fullscreen', True)
win.title('My wallet')
win.minsize(400, 480)
win.maxsize(960, 1080)
win['bg'] = '#3b5998'

data = {
                    'operation': 'withdraw',
                    'how much':100,
                    'comment': 'trololo',
                    'date': '10:30'
                }

for key in data.values():
    key = tk.Label(win, text=key).pack(side='left')
    key = tk.Label(win, text=key).pack(side='left')
    key = tk.Label(win, text=key).pack(side='left')
    key = tk.Label(win, text=key).pack(side='left')



win.mainloop()

for row in reader:
    # x = f"operation: {row['operation']}, how much: {row['how much']}, comment: {row['comment']}, date: {row['date']}"
    if row['operation'] == 'refill':
        # tk.Label(win3, text=x, fg='green', bg='white').pack(anchor='w')
        for key in row.values():
            tk.Label(win3, text=key, fg='green', bg='white').pack(side='left')
            tk.Label(win3, text=key, fg='green', bg='white').pack(side='left')
            tk.Label(win3, text=key, fg='green', bg='white').pack(side='left')
            tk.Label(win3, text=key, fg='green', bg='white').pack(side='left')
            tk.Label(win3, text='', bg='white').pack(side='left')
    else:
        # tk.Label(win3, text=x, fg='red', bg='white').pack(anchor='w')
        for key in row.values():
            tk.Label(win3, text=key, fg='red', bg='white').pack(side='left')
            tk.Label(win3, text=key, fg='red', bg='white').pack(side='left')
            tk.Label(win3, text=key, fg='red', bg='white').pack(side='left')
            tk.Label(win3, text=key, fg='red', bg='white').pack(side='left')
            tk.Label(win3, text='', bg='white').pack(side='left')

    with open('categories\\common_history.csv', 'r', encoding="utf-8") as file:
        order = ['operation', 'how much', 'comment', 'date']
        reader = csv.DictReader(file, fieldnames=order)
        for row in reader:
            #x = f"operation: {row['operation']}, how much: {row['how much']}, comment: {row['comment']}, date: {row['date']}"
            x1 = row['operation']
            x2 = row['how much']
            x3 = row['comment']
            x4 = row['date']
            if row['operation'] == 'refill':
                #tk.Label(win3, text=x, fg='green', bg='white').pack(anchor='w')
                tk.Label(win3, text=x1, fg='green', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text=x2, fg='green', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text=x3, fg='green', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text=x4, fg='green', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text='\n', anchor='nw').pack(side='bottom')
            else:
                #tk.Label(win3, text=x, fg='red', bg='white').pack(anchor='w')
                tk.Label(win3, text=x1, fg='red', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text=x2, fg='red', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text=x3, fg='red', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text=x4, fg='red', bg='white', anchor='nw').pack(side='left')
                tk.Label(win3, text='\n', anchor='nw').pack(side='bottom')