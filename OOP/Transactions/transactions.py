import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 2)

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    corrected_price = cell.value * 0.9              # we need to get 90% of our current prices to the D column
    corrected_price_cell = sheet.cell(row, 4)       # D column's number is 4
    corrected_price_cell.value = corrected_price

wb.save('transactions2.xlsx')                       # we created new file in our directory
