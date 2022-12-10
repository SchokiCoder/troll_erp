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

#generic definitions
APP_NAME = "Troll ERP"
APP_MAJOR = 1
APP_MINOR = 0
APP_PATCH = 0

APP_LICENSE = """Copyright (C) 2021 Andy Frank Schoknecht

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, only version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

#path defintions
PATH_DB = "troll.db"
PATH_CFG = "config.ini"

#sql scripts
SQL_BUILD_DB = """
--allow foreign keys in this database
PRAGMA foreign_keys = ON;

--create tables
CREATE TABLE tbl_parts(
    part_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,  --internal db id
    part_name VARCHAR(64),
    part_number VARCHAR(20) UNIQUE,
    amount INTEGER NOT NULL,                                    --determines storage_date and removal_date by being equal to or less than 1
    shelf_number INT NOT NULL,                                  --unbound number to a shelf
    compartment_number INT NOT NULL,                            --unbound number to compartment
    storage_date REAL NOT NULL,                                 --date as Julian day number (automatically written by program)
    removal_date REAL                                           --date as Julian day number (automatically written by program)
);

CREATE TABLE tbl_shelf_cfg(
    shelf_rows INTEGER NOT NULL,              --amount of shelf rows in storage facility
    shelf_cols INTEGER NOT NULL,              --amount of shelf columns in storage facility
    shelf_compartments INTEGER NOT NULL       --amount of shelf compartments for each shelf
);

--add indexes
CREATE INDEX idx_part_id ON tbl_parts(part_id);
CREATE INDEX idx_part_number ON tbl_parts(part_number);

--add record to shelf cfg
INSERT INTO tbl_shelf_cfg (shelf_rows, shelf_cols, shelf_compartments)
VALUES (0, 0, 0);

--add trigger to prevent adding or removing rows from shelf cfg
--CREATE TRIGGER tgr_const_table_rows
--INSTEAD OF INSERT INTO OF tbl_shelf_cfg OR DELETE OF tbl_shelf_cfg
--BEGIN
--    RAISE(IGNORE)
--END;
"""
