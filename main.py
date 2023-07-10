#!/usr/bin/python3
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
import os.path
import tkinter as tk
from tkinter import ttk
import constants
import lang
import interface


class App(object):
    """
    Main entrance
    """
    def init_sidebar(self):
        self.sidebar_panel = tk.Frame(self.root)
        self.sidebar_panel.place(x=0, y=0, width=50,
                                 relheight=1.0)
        self.sidebar_homepage_button = ttk.Button(self.sidebar_panel,
                                                  text=lang.trans("sidebar.home"),
                                                  command=self.interfaces.homepage.init())
        self.sidebar_homepage_button.place(x=0, y=0,
                                           relwidth=1.0,
                                           height=50)

    def __init__(self):
        if not os.path.exists(os.path.abspath(".\\settings.json")):
            """
            If the configuration file does not exist, it indicates that it is used for the first time.
            """
            import oobe  # Run OOBE module.
        import settings
        self.root = tk.Tk(constants.NAME)
        self.root.title(constants.NAME + " " + constants.VERSION)
        self.root.geometry("720x480")
        self.root.resizable(False, False)
        self.width = 720
        self.height = 480
        self.interfaces = constants.Namespace()
        self.interfaces.homepage = interface.HomePage(self)
        if settings.settings.get("default_page") == 0:
            self.interfaces.homepage.init()
        elif settings.settings.get("default_page") == 1:
            pass
        self.init_sidebar()
        self.root.mainloop()


def main():
    if __name__ == "__main__":
        App()
