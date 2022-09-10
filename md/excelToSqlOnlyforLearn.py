import pandas as pd
import pyodbc
import tkinter as tk
from tkinter import filedialog


svr_name = 'localhost, 1433'
u_name = 'as'
u_password = '123456a@'

root = tk.Tk()

root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path)

data_frame = pd.read_excel(file_path)

df = pd.DataFrame(data_frame)


try:
    connectSever = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}' +
                                  ';SERVER=' + 'localhost, 1433' +
                                  #   ';Database= QLSV' +
                                  ';UID=' + 'sa' +
                                  ';PWD=' + '123456a@;' +
                                  'Authentication type = SQL Login;')
except NameError:
    print(NameError)

print('accept connect')

cursor = connectSever.cursor()
cursor.execute('USE QLSV')


cursor.execute('SELECT * FROM SinhVien')
list1 = ['MaSV', 'HotenSV', 'GioiTinh', 'NgaySinh', 'QueQuan', 'Email']

for row in df.itertuples():
    sql = '''INSERT INTO SINHVIEN ({}) VALUES ({})'''.format(
        ','.join(list1), ','.join(['?']*len(df.columns)))
    cursor.execute(sql, tuple(row[1:]))


# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO SINHVIEN (MaSV, HotenSV ,GioiTinh , NgaySinh, QueQuan, Email)
#                 VALUES (?,?,?,?,?,?)
#                 ''',
#                 row.MaSV,
#                 row.HoTenSV,
#                 row.gioitinh,
#                 row.ngaysinh,
#                 row.QueQuan,
#                 row.email
#                 )


# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO MONHOC (MaMH, tenMH ,DVHT)
#                 VALUES (?,?,?)
#                 ''',
#                 row.MaMH,
#                 row.TenMH,
#                 row.DVHT
#                 )

cursor.commit()
