import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 2)

for row in range(1, sheet.max_row + 1):
    print(row)                              # 1 \n 2 \n 3 \n 4
