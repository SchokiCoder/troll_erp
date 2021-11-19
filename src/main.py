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

import application

#main
if __name__ == "__main__":
    
    #declare variables
    app = application.Application()

    #init app
    app.init()

    #start app
    app.mainloop()