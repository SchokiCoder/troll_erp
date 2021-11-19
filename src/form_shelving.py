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

import tkinter
import tkinter.messagebox

class FrmShelving:

    #members
    app = None
    lbl_title = tkinter.Label
    lbl_rows = tkinter.Label
    lbl_cols = tkinter.Label
    lbl_compartments = tkinter.Label
    txt_rows = tkinter.Entry
    txt_cols = tkinter.Entry
    txt_compartments = tkinter.Entry
    btn_save = tkinter.Button

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
        self.lbl_rows = tkinter.Label(self.app.box_main)
        self.lbl_cols = tkinter.Label(self.app.box_main)
        self.lbl_compartments = tkinter.Label(self.app.box_main)
        self.txt_cols = tkinter.Entry(self.app.box_main)
        self.txt_rows = tkinter.Entry(self.app.box_main)
        self.txt_compartments = tkinter.Entry(self.app.box_main)
        self.btn_save = tkinter.Button(self.app.box_main)

        #set widget values
        self.lbl_title["text"] = self.app.language["title_shelving"]
        self.lbl_rows["text"] = self.app.language["rows"]
        self.lbl_cols["text"] = self.app.language["columns"]
        self.lbl_compartments["text"] = self.app.language["compartments"]
        self.btn_save["text"] = self.app.language["save"]

        #bind commands
        self.btn_save.bind("<Button-1>", self.save)

        #place own widgets into main frame
        self.lbl_title.grid(
            column = 0,
            row = 0,
            sticky = "w",
            pady = (0, 10)
        )

        self.lbl_cols.grid(
            column = 0,
            row = 1,
            sticky = "w"
        )

        self.txt_cols.grid(
            column = 1,
            row = 1,
            sticky = "w"
        )

        self.lbl_rows.grid(
            column = 0,
            row = 2,
            sticky = "w"
        )

        self.txt_rows.grid(
            column = 1,
            row = 2,
            sticky = "w"
        )

        self.lbl_compartments.grid(
            column = 0,
            row = 3,
            sticky = "w"
        )

        self.txt_compartments.grid(
            column = 1,
            row = 3,
            sticky = "w"
        )

        self.btn_save.grid(
            column = 0,
            row = 4,
            sticky = "w",
            padx = 20
        )

        #load shelving values from db
        sql = """
        SELECT *
        FROM tbl_shelf_cfg
        """
        
        shelf_cfg_values = self.app.db.execute(sql).fetchall()[0]

        self.txt_rows.insert(0, str(shelf_cfg_values[0]))
        self.txt_cols.insert(0, str(shelf_cfg_values[1]))
        self.txt_compartments.insert(0, str(shelf_cfg_values[2]))
    
    def save(self, dummy):

        #get values
        raw_rows = self.txt_rows.get()
        raw_cols = self.txt_cols.get()
        raw_compartments = self.txt_compartments.get()

        #parse to numbers
        try:
            rows = int(raw_rows)
            cols = int(raw_cols)
            compartments = int(raw_compartments)
        
        except:
            tkinter.messagebox.showerror(self.app.language["error"], self.app.language["err_shelving_types"])
            return
        
        #save to db
        sql = """
        UPDATE tbl_shelf_cfg
        SET shelf_rows = ?, shelf_cols = ?, shelf_compartments = ?;
        """

        self.app.db.execute(sql, [rows, cols, compartments])
        self.app.db.commit()
