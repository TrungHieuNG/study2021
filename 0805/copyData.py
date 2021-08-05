import openpyxl
wb = openpyxl.load_workbook("0805.xlsx")
ws_hello = wb["hello"]
ws_hello2 = wb["hello2"]
wb.save("0805.xlsx")

