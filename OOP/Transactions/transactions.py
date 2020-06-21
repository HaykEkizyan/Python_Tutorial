import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 2)

for row in range(2, sheet.max_row + 1):   # start from 2 for ignore 1st row: "price"
    cell = sheet.cell(row, 3)             # 3 is a number of column
    print(cell.value)                     # 5.95 \n 6.95 \n 7.95
