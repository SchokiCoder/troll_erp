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

from time import strftime
import time
import tkinter
import tkinter.messagebox
import tkinter.ttk
import datetime

class FrmParts:

    #members
    app = None
    lbl_title = tkinter.Label
    lbl_selection = tkinter.Label
    cbo_selection = tkinter.ttk.Combobox
    lbl_part_name = tkinter.Label
    lbl_part_number = tkinter.Label
    lbl_amount = tkinter.Label
    lbl_shelf_number = tkinter.Label
    lbl_compartment_number = tkinter.Label
    lbl_storage_date = tkinter.Label
    lbl_removal_date = tkinter.Label
    txt_part_name = tkinter.Entry
    txt_part_number = tkinter.Entry
    txt_amount = tkinter.Entry
    txt_shelf_number = tkinter.Entry
    txt_compartment_number = tkinter.Entry
    txt_storage_date = tkinter.Entry
    txt_removal_date = tkinter.Entry
    box_buttons = tkinter.Frame
    btn_save = tkinter.Button
    btn_new = tkinter.Button

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
        self.lbl_selection = tkinter.Label(self.app.box_main)
        self.cbo_selection = tkinter.ttk.Combobox(self.app.box_main)
        self.lbl_part_name = tkinter.Label(self.app.box_main)
        self.lbl_part_number = tkinter.Label(self.app.box_main)
        self.lbl_amount = tkinter.Label(self.app.box_main)
        self.lbl_shelf_number = tkinter.Label(self.app.box_main)
        self.lbl_compartment_number = tkinter.Label(self.app.box_main)
        self.lbl_storage_date = tkinter.Label(self.app.box_main)
        self.lbl_removal_date = tkinter.Label(self.app.box_main)
        self.txt_part_name = tkinter.Entry(self.app.box_main)
        self.txt_part_number = tkinter.Entry(self.app.box_main)
        self.txt_amount = tkinter.Entry(self.app.box_main)
        self.txt_shelf_number = tkinter.Entry(self.app.box_main)
        self.txt_compartment_number = tkinter.Entry(self.app.box_main)
        self.txt_storage_date = tkinter.Entry(self.app.box_main)
        self.txt_removal_date = tkinter.Entry(self.app.box_main)
        self.box_buttons = tkinter.Frame(self.app.box_main)
        self.btn_save = tkinter.Button(self.box_buttons)
        self.btn_new = tkinter.Button(self.box_buttons)

        #set widget values
        self.lbl_title["text"] = self.app.language["title_parts"]
        self.lbl_selection["text"] = self.app.language["selection"]
        self.lbl_part_name["text"] = self.app.language["part_name"]
        self.lbl_part_number["text"] = self.app.language["part_number"]
        self.lbl_amount["text"] = self.app.language["amount"]
        self.lbl_shelf_number["text"] = self.app.language["shelf_number"]
        self.lbl_compartment_number["text"] = self.app.language["compartment_number"]
        self.lbl_storage_date["text"] = self.app.language["storage_date"]
        self.lbl_removal_date["text"] = self.app.language["removal_date"]
        self.btn_save["text"] = self.app.language["save"]
        self.btn_new["text"] = self.app.language["new"]

        #bind commands
        self.btn_save.bind("<Button-1>", self.save)
        self.cbo_selection.bind("<<ComboboxSelected>>", self.load_tuple)

        #place own widgets into main frame
        self.lbl_title.grid(
            column = 0,
            row = 0,
            sticky = "w",
            pady = (0, 10)
        )

        self.lbl_selection.grid(
            column = 0,
            row = 1,
            sticky = "w",
            pady = (0, 20)
        )

        self.cbo_selection.grid(
            column = 1,
            row = 1,
            sticky = "w",
            pady = (0, 20)
        )
        
        self.lbl_part_name.grid(
            column = 0,
            row = 2,
            sticky = "w"
        )

        self.txt_part_name.grid(
            column = 1,
            row = 2,
            sticky = "w"
        )

        self.lbl_part_number.grid(
            column = 0,
            row = 3,
            sticky = "w"
        )

        self.txt_part_number.grid(
            column = 1,
            row = 3,
            sticky = "w"
        )

        self.lbl_amount.grid(
            column = 0,
            row = 4,
            sticky = "w"
        )

        self.txt_amount.grid(
            column = 1,
            row = 4,
            sticky = "w"
        )

        self.lbl_shelf_number.grid(
            column = 0,
            row = 5,
            sticky = "w"
        )

        self.txt_shelf_number.grid(
            column = 1,
            row = 5,
            sticky = "w"
        )

        self.lbl_compartment_number.grid(
            column = 0,
            row = 6,
            sticky = "w"
        )

        self.txt_compartment_number.grid(
            column = 1,
            row = 6,
            sticky = "w"
        )

        self.lbl_storage_date.grid(
            column = 0,
            row = 7,
            sticky = "w"
        )

        self.txt_storage_date.grid(
            column = 1,
            row = 7,
            sticky = "w"
        )

        self.lbl_removal_date.grid(
            column = 0,
            row = 8,
            sticky = "w"
        )

        self.txt_removal_date.grid(
            column = 1,
            row = 8,
            sticky = "w"
        )

        self.box_buttons.grid(
            column = 0,
            row = 9,
            columnspan = 2,
            sticky = "w",
            pady = (10, 0)
        )

        self.btn_save.grid(
            column = 0,
            row = 0,
            sticky = "w",
            padx = (0, 30)
        )

        self.btn_new.grid(
            column = 1,
            row = 0,
            sticky = "w",
            padx = (0, 30)
        )

        self.refresh_selection()

    def refresh_selection(self, dummy = 0):

        #load parts into selection
        sql = """
        SELECT (part_id || ": " || part_name || ", " || part_number)
        FROM tbl_parts
        """
        data = self.app.db.execute(sql).fetchall()
        parts = []

        for row in data:
            parts.append(row[0])
        
        self.cbo_selection.configure(values = parts)
    
    def load_tuple(self, dummy):
        
        #get selected part
        part = self.cbo_selection.get()
        part = part.split(":")[0]
        
        #load tuple from db
        sql = """
        SELECT part_name, part_number, amount, shelf_number, compartment_number, date(storage_date), date(removal_date)
        FROM tbl_parts
        WHERE part_id = ?;
        """
        data = self.app.db.execute(sql, [part]).fetchall()[0]

        #put data into fields
        self.txt_part_name.delete(0, "end")
        self.txt_part_name.insert(0, data[0])
        self.txt_part_number.delete(0, "end")
        self.txt_part_number.insert(0, data[1])
        self.txt_amount.delete(0, "end")
        self.txt_amount.insert(0, data[2])
        self.txt_shelf_number.delete(0, "end")
        self.txt_shelf_number.insert(0, data[3])
        self.txt_compartment_number.delete(0, "end")
        self.txt_compartment_number.insert(0, data[4])
        self.txt_storage_date.delete(0, "end")
        self.txt_storage_date.insert(0, data[5])
        self.txt_removal_date.delete(0, "end")
        if data[6] != None:
            self.txt_removal_date.insert(0, data[6])

    def save(self, dummy):

        #declare variables
        error_msg = ""

        #get values
        idx_selection = self.cbo_selection.current()
        selection = self.cbo_selection.get().split(":")[0]
        raw_part_name = self.txt_part_name.get()
        raw_part_number = self.txt_part_number.get()
        raw_amount = self.txt_amount.get()
        raw_shelf_number = self.txt_shelf_number.get()
        raw_compartment_number = self.txt_compartment_number.get()
        raw_storage_date = self.txt_storage_date.get()
        raw_removal_date = ""

        #sanitize values
        if len(raw_part_name) > 64:
            error_msg += self.app.language["err_part_name_length"] + "\n"
        
        if len(raw_part_number) > 20:
            error_msg += self.app.language["err_part_number_length"] + "\n"
        
        try:
            amount = int(raw_amount)
        except:
            error_msg += self.app.language["err_amount_type"] + "\n"

        try:
            shelf_number = int(raw_shelf_number)
        except:
            error_msg += self.app.language["err_shelf_number_type"] + "\n"

        try:
            compartment_number = int(raw_compartment_number)
        except:
            error_msg += self.app.language["err_compartment_number_type"] + "\n"
        
        #if values are not correct, print error and stop
        if error_msg != "":
            tkinter.messagebox.showerror(self.app.language["error"], error_msg)
            return

        #if storage date is not given, get current date
        if raw_storage_date == "":
            raw_storage_date = datetime.date.today()

        #if amount is zero, get current date as removal date
        if amount == 0:
            raw_removal_date = datetime.date.today()

        #find out if insert or update is needed
        if idx_selection == -1:
            #insert
            sql = """
            INSERT INTO tbl_parts (part_name, part_number, amount, shelf_number, compartment_number, storage_date, removal_date)
            VALUES (?, ?, ?, ?, ?, julianday(?), julianday(?));
            """

            self.app.db.execute(sql, [raw_part_name, raw_part_number, amount, shelf_number, compartment_number, raw_storage_date, raw_removal_date])
            self.app.db.commit()
        
        else:
            #update
            sql = """
            UPDATE tbl_parts
            SET part_name = ?, part_number = ?, amount = ?, shelf_number = ?, compartment_number = ?, storage_date = julianday(?), removal_date = julianday(?)
            WHERE part_id = ?;
            """

            self.app.db.execute(sql, [raw_part_name, raw_part_number, amount, raw_storage_date, raw_removal_date, selection])
            self.app.db.commit()

        self.refresh_selection()
