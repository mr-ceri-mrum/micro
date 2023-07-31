import openpyxl
import sqlite3

def write_data_to_database(file_path, table_name):
    book = openpyxl.open(file_path, read_only=True)
    sheet = book.active

   
    connection = sqlite3.connect('database.db') 
    cursor = connection.cursor()
    
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, name TEXT)")

   
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Пропускаем первую строку с заголовками (min_row=2)
        id_value = row[0]
        name_value = row[1]
        cursor.execute(f"INSERT INTO {table_name} (id, name) VALUES (?, ?)", (id_value, name_value))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    file_path = "Data.xlsx" 
    table_name = "my_table" 

file_path = "Data.xlsx"
table_name = "DataDase.db"
write_data_to_database(file_path, table_name)
