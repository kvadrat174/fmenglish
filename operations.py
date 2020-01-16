import oauth2client
import gspread
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time








scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

gc = gspread.authorize(credentials)

sh = gc.open("fmenglish")



class uchenik:
    def __init__(self, age,group, teacher):
        self.age = age
        self.teacher = teacher
        self.group = group
    def find_groups(self):
        wks = sh.worksheet('groups')
        res = wks.findall(self)
        for i in res:
            ro = i.row
            b = wks.cell(ro, 2).value
            return b


    def vizit(self):
        wks = sh.worksheet('students')
        d = datetime.datetime.today().strftime("%Y-%m-%d")
        var = wks.row_values(self)
        a= len(var) + 1
        wks.update_cell(self,a,d)
        kl = var[5]
        return kl

    def nvizit(self):
        wks = sh.worksheet('students')
        d = 'не был'
        var = wks.row_values(self)
        a= len(var) + 1
        wks.update_cell(self,a,d)
        kl = var[5]
        return kl

    def get_stlist(self):
        wks = sh.worksheet('students')
        res = wks.findall(self)

        stud = list()

        for i in res:
            rr = i.row

            ro = wks.row_values(i.row, value_render_option='FORMATTED_VALUE')
            d = datetime.datetime.today().strftime("%Y-%m-%d")
            m =  'не был'
            if d not in ro and m not in ro:


                print(i.row)
                name = ro[0]
                stud.append(name)
                surname = ro[1]
                stud.append(surname)
                b = ' '.join(stud)


                return b, rr
            else:

                continue



def save_std(name, surname, group):
    wks = sh.worksheet('students')
    ro = len(wks.col_values(1)) + 1
    wks.update_cell(ro, 1, name)
    wks.update_cell(ro, 2, surname)
    wks.update_cell(ro, 6, group)

def UserList(id1,nm):
    wks = sh.worksheet('teachers')

    values_list = wks.col_values(2, value_render_option='UNFORMATTED_VALUE')
    if id1 in values_list:

        return True

    elif id1 not in values_list:

        return False;


