import openpyxl as xl                                 # import openpyxl lets us work with Pypi libraries, which include also spreadsheet tools
wb = xl.load_workbook('transactions.xlsx')            # transactions.xlsx file is with app.py file in the current project
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(2, 1)

