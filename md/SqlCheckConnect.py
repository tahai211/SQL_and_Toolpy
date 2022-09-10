import tkinter as tk
import pandas as pd
from sqlalchemy import create_engine
import pyodbc

svr_name = 'sql1'
db_name = 'QLSV'
u_name = 'as'
u_password = '123456a@'

try:
    connectSever = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}' +
                                  ';SERVER=' + 'localhost, 1433' +
                                #   ';Database= QLSV' +
                                  ';UID=' + 'sa' +
                                  ';PWD=' + '123456a@;'+
                                  'Authentication type = SQL Login;')
    print("connection successfull")
except NameError:
    print ("connection failed")

print('accept connect')

cursor = connectSever.cursor()
cursor.execute('USE QLSV')
cursor.execute('SELECT * FROM SinhVien')



for row in cursor:
    print('row = %r\n' % (row,))

cursor.execute('SP_COLUMNS MONHOC')

list_Column = []

for row in cursor:
    list_Column.append(row)

print(list_Column)