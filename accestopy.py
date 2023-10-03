import pyodbc
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Admin\\Documents\\30A\\acces_to_py\\db.accdb;')
cursor = conn.cursor() # создается курсор
cursor.execute("select *from table1")
for string in cursor.fetchall():
  print(string)  # Выводятся строки базы данных.

# import pyodbc;

# msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
# print(msa_drivers)