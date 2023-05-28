import os.path
import tkinter
from tkinter import ttk

import lang

"""
Init program config files.
"""
f = open(os.path.abspath(".\\settings.json"), mode="x")
f.write("""{\n    "default_page": 0\n}\n""")
f.close()

root = tkinter.Tk(lang.trans("oobe.welcome"))
root.geometry("720x480")
root.title(lang.trans("oobe.welcome"))
welcome_label = tkinter.Label(root, text=lang.trans("oobe.welcome"))
welcome_label.pack()
root.mainloop()

