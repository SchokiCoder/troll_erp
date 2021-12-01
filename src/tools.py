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

from typing import Dict

def read_ini_file(p_path: str) -> Dict:
    
    #declare variables
    result = {}
    temp = []

    #open file, read content, close file
    try:
        file = open(p_path, "r")
    except:
        return result
    content = file.readlines()
    file.close()

    #parse
    for line in content:
        temp = line.split("=")
        result[temp[0].strip()] = temp[1].strip()
    
    #return
    return result

def write_ini_file(p_path: str, p_content: Dict):

    #open file
    file = open(p_path, "w")

    #write    
    for key in p_content.keys():
        file.write(key + "=" + p_content[key] + "\n")
    
    #close file
    file.close()
