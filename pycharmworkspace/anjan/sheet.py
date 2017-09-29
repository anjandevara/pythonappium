import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds']


# json credentials you downloaded earlier
# get email and key from creds
credentials = ServiceAccountCredentials.from_json_keyfile_name('BugsList.json', scope)

# authenticate with Google
client = gspread.authorize(credentials)

# open sheet
sheet = client.open("BugsList").sheet1

pp = pprint.PrettyPrinter()

bugslist = sheet.get_all_records()

pp.pprint(bugslist)

print('\n')

bugslist_row = sheet.row_values(6)
pp.pprint(bugslist_row)

print('\n')

bugslist_col = sheet.col_values(5)
pp.pprint(bugslist_col)

print('\n')

bugs_cell = sheet.cell(6,3).value
pp.pprint(bugs_cell)

row_add = ["Hello", "How are you?"]
sheet.insert_row(row_add)

