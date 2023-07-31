# Чтение данных из Excel
import openpyxl
import sqlite3

table_name = "newData"

book = openpyxl.open("Data.xlsx", read_only=True)

sheet = book.active

for row in range(1, sheet.max_row + 1):
    id = sheet[row][0].value
    name = sheet[row][1].value
    print(row, id, name)

for row in range(2, sheet.max_row + 1):
    id = sheet[row][0].value
    name = sheet[row][1].value
    print(row, id, name)