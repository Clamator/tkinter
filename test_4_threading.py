import time
import threading
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self,command=self.start_action,
                                text="Ждать 5 секунд")
        self.button.place(x=50, y=70, width=150, height=30)
        self.button = tk.Button(self, command=self.start_action,
                                text="Ждать 10 секунд")
        self.button.place(x=200, y=70, width=150, height=30)

        self.entry = tk.Entry(self, ).place(x=50, y=30, width=150, height=30)
        self.entry = tk.Entry(self, ).place(x=200, y=30, width=150, height=30)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        thread = threading.Thread(target=self.run_action)

        print(threading.main_thread().name)
        print(thread.name)
        thread.start()
        self.label = tk.Label(self, text='запуск действия').place(x=50, y=110, width=150, height=30)
        self.label = tk.Label(self, text='запуск действия').place(x=200, y=110, width=150, height=30)
        self.check_thread(thread)

    def check_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.check_thread(thread))
        else:
            self.button.config(state=tk.NORMAL)

    def run_action(self):
        print("Запуск длительного действия...")
        time.sleep(4)
        self.label = tk.Label(self, text='действие завершено').place(x=50, y=110, width=150, height=30)
        self.label = tk.Label(self, text='действие завершено').place(x=200, y=110, width=150, height=30)
        print("Длительное действие завершено!")

if __name__ == "__main__":
    app = App()
    app.geometry('400x300+300+200')
    app.resizable(width=False, height=False)
    app.mainloop()