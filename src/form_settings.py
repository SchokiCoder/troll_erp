#    Troll ERP
#    Copyright (C) 2021  Andy Frank Schoknecht
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import constants
import languages
import tkinter
import tkinter.ttk
import tools

class FrmSettings:

    #members
    app = None
    lbl_title = tkinter.Label
    lbl_language = tkinter.Label
    cbo_language = tkinter.ttk.Combobox

    #constructor
    def __init__(self, p_app):
        
        #save values
        self.app = p_app
    
    #show function
    def show(self):

        #clear window main frame
        self.app.clear_frame()

        #initialize widgets
        self.lbl_title = tkinter.Label(self.app.box_main)
        self.lbl_language = tkinter.Label(self.app.box_main)
        self.cbo_language = tkinter.ttk.Combobox(self.app.box_main)

        #set widget values
        self.lbl_title["text"] = self.app.language["title_settings"]
        self.lbl_language["text"] = self.app.language["language"]

        #bind commands
        self.cbo_language.bind("<<ComboboxSelected>>", self.save)

        #place own widgets into main frame
        self.lbl_title.grid(
            column = 0,
            row = 0,
             sticky = "w"
        )

        self.lbl_language.grid(
            column = 0,
            row = 1
        )

        self.cbo_language.grid(
            column = 1,
            row = 1
        )

        #put language options into cbo
        self.cbo_language.configure(values = ["English", "Deutsch"])

        #set current values
        self.cbo_language.delete(0, "end")
        if self.app.language == languages.english:
            self.cbo_language.insert(0, "English")
        elif self.app.language == languages.german:
            self.cbo_language.insert(0, "Deutsch")
    
    def save(self, dummy):
        
        #get values
        raw_language = self.cbo_language.get()
        language = raw_language.strip()

        #if given language doesn't exist, stop
        if language != "English" and language != "Deutsch":
            return

        #save to cfg
        cfg = {}
        cfg["language"] = language
        tools.write_ini_file(constants.PATH_CFG, cfg)
