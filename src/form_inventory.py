# Troll ERP
# Copyright (C) 2021 - 2022  Andy Frank Schoknecht
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not see
# <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>.

import tkinter

class FrmInventory:

    #member
    app = None
    lbl_title = tkinter.Label
    lbl_filters = tkinter.Label
    box_filters = tkinter.Frame
    lbl_filter_part_name = tkinter.Label
    lbl_filter_part_number = tkinter.Label
    lbl_filter_shelf_number = tkinter.Label
    lbl_filter_compartment_number = tkinter.Label
    lbl_filter_storage_date_begin = tkinter.Label
    lbl_filter_storage_date_end = tkinter.Label
    lbl_filter_removal_date_begin = tkinter.Label
    lbl_filter_removal_date_end = tkinter.Label
    txt_filter_part_name = tkinter.Entry
    txt_filter_part_number = tkinter.Entry
    txt_filter_shelf_number = tkinter.Entry
    txt_filter_compartment_number = tkinter.Entry
    txt_filter_storage_date_begin = tkinter.Entry
    txt_filter_storage_date_end = tkinter.Entry
    txt_filter_removal_date_begin = tkinter.Entry
    txt_filter_removal_date_end = tkinter.Entry
    btn_refresh = tkinter.Button
    lbl_output = tkinter.Label
    box_output = tkinter.Frame

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
        self.lbl_filters = tkinter.Label(self.app.box_main)
        self.box_filters = tkinter.Frame(self.app.box_main)
        self.lbl_filter_part_name = tkinter.Label(self.box_filters)
        self.lbl_filter_part_number = tkinter.Label(self.box_filters)
        self.lbl_filter_shelf_number = tkinter.Label(self.box_filters)
        self.lbl_filter_compartment_number = tkinter.Label(self.box_filters)
        self.lbl_filter_storage_date_begin = tkinter.Label(self.box_filters)
        self.lbl_filter_storage_date_end = tkinter.Label(self.box_filters)
        self.lbl_filter_removal_date_begin = tkinter.Label(self.box_filters)
        self.lbl_filter_removal_date_end = tkinter.Label(self.box_filters)
        self.txt_filter_part_name = tkinter.Entry(self.box_filters)
        self.txt_filter_part_number = tkinter.Entry(self.box_filters)
        self.txt_filter_shelf_number = tkinter.Entry(self.box_filters)
        self.txt_filter_compartment_number = tkinter.Entry(self.box_filters)
        self.txt_filter_storage_date_begin = tkinter.Entry(self.box_filters)
        self.txt_filter_storage_date_end = tkinter.Entry(self.box_filters)
        self.txt_filter_removal_date_begin = tkinter.Entry(self.box_filters)
        self.txt_filter_removal_date_end = tkinter.Entry(self.box_filters)
        self.btn_refresh = tkinter.Button(self.box_filters)
        self.lbl_output = tkinter.Label(self.app.box_main)
        self.box_output = tkinter.Frame(self.app.box_main)

        #set widget values
        self.lbl_title["text"] = self.app.language["title_inventory"]
        self.lbl_filters["text"] = self.app.language["filters"]
        self.lbl_filter_part_name["text"] = self.app.language["part_name"]
        self.lbl_filter_part_number["text"] = self.app.language["part_number"]
        self.lbl_filter_shelf_number["text"] = self.app.language["shelf_number"]
        self.lbl_filter_compartment_number["text"] = self.app.language["compartment_number"]
        self.lbl_filter_storage_date_begin["text"] = self.app.language["storage_date"] + " (" + self.app.language["begin"] + ")"
        self.lbl_filter_storage_date_end["text"] = self.app.language["storage_date"] + " (" + self.app.language["end"] + ")"
        self.lbl_filter_removal_date_begin["text"] = self.app.language["removal_date"] + " (" + self.app.language["begin"] + ")"
        self.lbl_filter_removal_date_end["text"] = self.app.language["removal_date"] + " (" + self.app.language["end"] + ")"
        self.btn_refresh["text"] = self.app.language["refresh"]
        self.lbl_output["text"] = self.app.language["output"]

        #bind commands
        self.btn_refresh.bind("<Button-1>", self.refresh_output)

        #place own widgets into main frame
        self.lbl_title.grid(
            column = 0,
            row = 0,
            sticky = "w",
            pady = (0, 10)
        )

        self.lbl_filters.grid(
            column = 0,
            row = 1,
            sticky = "w"
        )

        self.box_filters.grid(
            column = 0,
            row = 2,
            sticky = "w",
        )

        self.lbl_filter_part_name.grid(
            column = 0,
            row = 0
        )

        self.lbl_filter_part_number.grid(
            column = 1,
            row = 0
        )

        self.lbl_filter_shelf_number.grid(
            column = 2,
            row = 0
        )

        self.lbl_filter_compartment_number.grid(
            column = 3,
            row = 0
        )

        self.lbl_filter_storage_date_begin.grid(
            column = 4,
            row = 0
        )

        self.lbl_filter_storage_date_end.grid(
            column = 5,
            row = 0
        )

        self.lbl_filter_removal_date_begin.grid(
            column = 6,
            row = 0
        )

        self.lbl_filter_removal_date_end.grid(
            column = 7,
            row = 0
        )

        self.txt_filter_part_name.grid(
            column = 0,
            row = 1
        )

        self.txt_filter_part_number.grid(
            column = 1,
            row = 1
        )

        self.txt_filter_shelf_number.grid(
            column = 2,
            row = 1
        )

        self.txt_filter_compartment_number.grid(
            column = 3,
            row = 1
        )

        self.txt_filter_storage_date_begin.grid(
            column = 4,
            row = 1
        )

        self.txt_filter_storage_date_end.grid(
            column = 5,
            row = 1
        )

        self.txt_filter_removal_date_begin.grid(
            column = 6,
            row = 1
        )

        self.txt_filter_removal_date_end.grid(
            column = 7,
            row = 1
        )

        self.btn_refresh.grid(
            column = 8,
            row = 1
        )

        self.lbl_output.grid(
            column = 0,
            row = 3,
            sticky = "w"
        )

        self.box_output.grid(
            column = 0,
            row = 4,
            sticky = "w",
        )
    
    def refresh_output(self, dummy):
        
        #empty output box
        for widget in self.box_output.winfo_children():
            widget.destroy()

        #get filter values
        filter_part_name = self.txt_filter_part_name.get()
        filter_part_number = self.txt_filter_part_number.get()
        filter_shelf_number = self.txt_filter_shelf_number.get()
        filter_compartment_number = self.txt_filter_compartment_number.get()
        filter_storage_date_begin = self.txt_filter_storage_date_begin.get()
        filter_storage_date_end = self.txt_filter_storage_date_end.get()
        filter_removal_date_begin = self.txt_filter_removal_date_begin.get()
        filter_removal_date_end = self.txt_filter_removal_date_end.get()

        #prepare sql string
        sql_parameters = []
        sql = """
        SELECT part_id, part_name, part_number, amount, shelf_number, compartment_number, date(storage_date), date(removal_date)
        FROM tbl_parts
        WHERE true"""

        if filter_part_name != "":
            sql += " and part_name = ?"
            sql_parameters.append(filter_part_name)

        if filter_part_number != "":
            sql += " and part_number = ?"
            sql_parameters.append(filter_part_number)

        if filter_shelf_number != "":
            sql += " and shelf_number = ?"
            sql_parameters.append(filter_shelf_number)

        if filter_compartment_number != "":
            sql += " and compartment_number = ?"
            sql_parameters.append(filter_compartment_number)

        if filter_storage_date_begin != "":
            sql += " and storage_date > julianday(?)"
            sql_parameters.append(filter_storage_date_begin)

        if filter_storage_date_end != "":
            sql += " and storage_date < julianday(?)"
            sql_parameters.append(filter_storage_date_end)

        if filter_removal_date_begin != "":
            sql += " and removal_date > julianday(?)"
            sql_parameters.append(filter_removal_date_begin)

        if filter_removal_date_end != "":
            sql += " and removal_date < julianday(?)"
            sql_parameters.append(filter_removal_date_end)
        
        #load data
        data = self.app.db.execute(sql, sql_parameters).fetchall()

        #put header into output box
        header = [
                self.app.language["id"],
                self.app.language["part_name"],
                self.app.language["part_number"],
                self.app.language["amount"],
                self.app.language["shelf_number"],
                self.app.language["compartment_number"],
                self.app.language["storage_date"],
                self.app.language["removal_date"]
                ]
        i = 0
        for item in header:
            temp = tkinter.Label(self.box_output)
            temp["text"] = item
            temp.grid(
                column = i,
                row = 0
            )
            i += 1

        #put data into output box
        y = 1
        for row in data:
            x = 0
            for item in row:
                temp = tkinter.Label(self.box_output)
                temp["text"] = item
                temp.grid(
                    column = x,
                    row = y
                )
                x += 1
            y += 1

