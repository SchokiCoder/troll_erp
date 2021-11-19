#Troll ERP
#Copyright (C) 2021 Andy Frank Schoknecht

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, only version 3 of the License.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

import constants
import languages
import tools
import form_parts
import form_inventory
import form_shelving
import form_settings
import os
import sys
import sqlite3
import tkinter
import tkinter.messagebox

class Application:

    #members
    language = {}
    cfg = {}
    db = sqlite3.Connection
    window = tkinter.Tk
    menu = tkinter.Menu
    box_main = tkinter.Frame
    frm_parts = form_parts.FrmParts
    frm_inventory = form_inventory.FrmInventory
    frm_shelving = form_shelving.FrmShelving
    frm_settings = form_settings.FrmSettings

    #clear frame function
    def clear_frame(self):

        for widget in self.box_main.winfo_children():
            widget.destroy()

    #init function
    def init(self):
        
        #declare variables
        create_db = False

        #read config
        self.cfg = tools.read_ini_file(constants.PATH_CFG)

        #set language
        if self.cfg.get("language") == "English":
            self.language = languages.english
        elif self.cfg.get("language") == "Deutsch":
            self.language = languages.german
        else:
            self.language = languages.english
        
        #initialize window, menu and main frame
        self.window = tkinter.Tk()
        self.window.title(constants.APP_NAME)
        self.menu = tkinter.Menu(self.window)
        self.box_main = tkinter.Frame(self.window)
        self.box_main.grid(
            padx = (10, 10),
            pady = (10, 10)
        )

        #set menu
        self.window["menu"] = self.menu

        #add menubar commands
        self.menu.add_command(label = self.language["title_parts"], command = lambda : self.frm_parts.show())
        self.menu.add_command(label = self.language["title_inventory"], command = lambda : self.frm_inventory.show())
        self.menu.add_command(label = self.language["title_shelving"], command = lambda : self.frm_shelving.show())
        self.menu.add_command(label = self.language["title_settings"], command = lambda : self.frm_settings.show())
        self.menu.add_command(label = self.language["title_about"],
            command = (lambda : tkinter.messagebox.showinfo("Info", constants.APP_NAME + " " +
                str(constants.APP_MAJOR) + "." + str(constants.APP_MINOR) + "." + str(constants.APP_PATCH) + "\n" +
                constants.APP_LICENSE)))

        #if db doesn't exist, warn user that new one is created
        if os.path.isfile(constants.PATH_DB) != True:
            tkinter.messagebox.showwarning(self.language["warning"], self.language["wrn_db_not_found"])
            create_db = True
        
        #connect to db
        try:
            self.db = sqlite3.connect(constants.PATH_DB)

            if create_db == True:
                self.db.executescript(constants.SQL_BUILD_DB)

        #if no conection, error message
        except:
            tkinter.messagebox.showerror(self.language["error"], self.language["err_con_db_failed"] + sys.argv[0][0 : sys.argv[0].rfind("/")] + "/" + constants.PATH_DB + "\"")
            raise FileNotFoundError("access to db file not allowed")

        #activate foreign keys
        self.db.execute("PRAGMA foreign_keys = ON;")

        #initialize forms
        self.frm_parts = form_parts.FrmParts(self)
        self.frm_inventory = form_inventory.FrmInventory(self)
        self.frm_shelving = form_shelving.FrmShelving(self)
        self.frm_settings = form_settings.FrmSettings(self)

    #mainloop
    def mainloop(self):
        
        #open parts menu
        self.frm_parts.show()

        #tk mainloop
        self.window.mainloop()
