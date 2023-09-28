#  ModLibrary, a Minecraft mod manager.
#  Copyright (C) 2023 iamliuzy
#
#  This file is part of ModLibrary.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#   any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see https://www.gnu.org/licenses/.

import tkinter
from pathlib import PurePath
from tkinter import ttk
import tkinter.filedialog
import lang
import mods


class Page(object):
    def __init__(self, main_class):
        self.main_class = main_class
        self.root = main_class.root
        self.window_width = main_class.width
        self.window_height = main_class.height
        self.panel = tkinter.Frame(self.root)


class HomePage(Page):
    def init(self):
        super().__init__(self)
        self.panel.place(x=50, y=0,
                         width=self.window_width - 50,
                         relheight=1.0)
        self.search_box_text = tkinter.StringVar()
        self.search_box_entry = ttk.Entry(master=self.panel,
                                          textvariable=self.search_box_text)
        self.search_box_entry.place(x=0, y=0, width=self.window_width - 80, height=30)
        self.add_button = ttk.Button(self.panel,
                                     text="+",
                                     command=self.add_mod)
        self.add_button.place(x=self.window_width - 80,
                              y=0, width=30, height=30)

    def add_mod(self):
        files = []
        for file in tkinter.filedialog.askopenfilenames(title=lang.trans("homepage.add_mod.title"),
                                                        filetypes=[("ModFile", "*.jar")]):
            files.append(mods.ModFile(PurePath(file)))
        if not files == []:
            mods.Mod(files)
        else:
            return

    def refresh(self):
        self.panel.destroy()
        self.panel = tkinter.Frame(self.root)
        self.init()




class Download(Page):
    def __init__(self):
        super.__init__(self)
