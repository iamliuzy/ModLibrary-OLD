import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import constants
import lang
import jsonparse


class App:
    def add_mod(self):
        tkinter.filedialog.askopenfilenames(title=lang._("homepage.add_mod.title"),
                                            filetypes=[("Mod", "*.jar")])

    def init_homepage(self):
        self.homepage_panel = tk.Frame(self.root)
        self.homepage_panel.place(x=50, y=0,
                                  width=self.root.winfo_width()-50,
                                  relheight=1.0)
        self.homepage_searchbox_text = tk.StringVar()
        self.homepage_searchbox_entry = ttk.Entry(self.homepage_panel,
                                                  textvariable=self.homepage_searchbox_text)
        self.homepage_searchbox_entry.place(x=0, y=0, width=self.root.winfo_width()-75, height=30)
        self.homepage_add_button = ttk.Button(self.homepage_panel,
                                              text="aaa",
                                              command=None)
        self.homepage_add_button.place(x=self.root.winfo_width()-50-self.homepage_searchbox_entry.winfo_width(),
                                       y=0, width=25, height=30)

    def init_sidebar(self):
        self.sidebar_panel = tk.Frame(self.root)
        self.sidebar_panel.place(x=0, y=0, width=50,
                                 relheight=1.0)
        self.sidebar_homepage_button = ttk.Button(self.sidebar_panel,
                                                  text=lang._("sidebar.home"),
                                                  command=self.init_homepage)
        self.sidebar_homepage_button.place(x=0, y=0,
                                           relwidth=1.0,
                                           height=50)

    def __init__(self):
        self.root = tk.Tk(constants.NAME)
        self.root.title(constants.NAME + " " + constants.VERSION)
        self.root.geometry("720x480+200+200")
        self.settings = jsonparse.QuickAccess.json_to_dict(".\\settings.json")
        if self.settings.get("default_page") == 0:
            self.init_homepage()
        elif self.settings.get("default_page") == 1:
            pass
        self.init_sidebar()
        self.root.mainloop()


App()
