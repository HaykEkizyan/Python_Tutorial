import openpyxl as xl
from openpyxl.chart import BarChart, Reference

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 2)

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    corrected_price = cell.value * 0.9              # we need to get 90% of our current prices to the D column
    corrected_price_cell = sheet.cell(row, 4)       # D column's number is 4
    corrected_price_cell.value = corrected_price

                                                    # use the Reference class to select a range for loop
values = Reference(sheet,                           # we add sheet argument
          min_row=2,
          max_row=sheet.max_row)                    # maximum row in this sheet

wb.save('transactions2.xlsx')                       # we created a new file in our directory
