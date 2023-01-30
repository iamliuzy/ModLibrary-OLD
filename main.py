import tkinter as tk
import constants


class App:
    def init_sidebar(self):
        self.sidebar_panel = tk.Frame(self.root)
        self.sidebar_download_button = tk.Button(self.sidebar_panel, command=None)

    def __init__(self):
        self.root = tk.Tk(constants.NAME)
        self.root.title(constants.NAME + " " + constants.VERSION)
        self.root.geometry("400x400+200+200")

        self.root.mainloop()


App()
