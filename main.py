# from infi.systray import SysTrayIcon
# def say_hello(systray):
#     print("Hello, World!")
# menu_options = (("Say Hello", None, say_hello),)
# systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
# systray.start()

import tkinter as tk


class Application(tk.Frame):
    quit_button = None

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()


app = Application()
app.master.title('Sample application')
app.mainloop()
