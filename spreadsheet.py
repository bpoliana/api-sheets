import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('cortesias.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Cortesias').sheet1

pp = pprint.PrettyPrinter()


row = ['1',
 'arabrab',
 '000111222-54',
 'bb@gmail.com',
 '(31)1234-1234',
 'O nome do vento',
 '123456',
 '123456']

index = 2 


sheet.delete_row(2)
# courtesies = sheet.get_all_records()
#courtesies = sheet.row_values(2)
courtesies = sheet.cell(2,6).value
pp.pprint(courtesies)

sheet.update_cell(2,6,'O temor do sabio')

courtesies = sheet.cell(2,6).value
pp.pprint(courtesies)