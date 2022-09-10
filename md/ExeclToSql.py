import pandas as pd
import pyodbc
import tkinter as tk
from tkinter import filedialog

svr_name = 'localhost, 1433'
usr_name = 'sa'
pwd_name = '123456a@'

#
# creat the connect with sql sẻver . với máy mac thì hình như phải tải ODBC
# , còn win thì đ sao hay sao ấy cứ DRIVER = SQL SERVER,SERVER = tên máy
# tại link sau ODBC : https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16
# tại đây mình dung bản 17
#
# #


def connectToServer():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}' +
                              ';SERVER='+svr_name +
                              ';UID='+usr_name +
                              ';PWD='+pwd_name +
                              ';Authentication type = SQL Login;')
        print("connection successfull")
        return conn
    except:
        print("connection failed")


conn = connectToServer()


#
# tạo con trỏ truy vấn cursor .execute để  viết lệnh sql thực thi ngay trên sql server
# ví dụ muốn dử dụng database nào ta dùng lệnh USE DATABASE
# #

db_name = input('---- Enter the name of Database : ')

cursor = conn.cursor()
cursor.execute('USE ' + db_name + '')
# cursor.execute('SELECT * FROM SINHVIEN')


#
# tạo giao diện chọn file từ tkinter, tôi đ biết gì về cái library nên nó hơi xấu
# #

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print('path of this excel file : ', end='')
print(file_path)


# pandas de doc du lieu tu Excel thanh cac dataframe
# #
data_frame = pd.read_excel(file_path)
df = pd.DataFrame(data_frame)

print('DataFram of this excel : ')
print(df)


# nhập tên table , kích thươcs và các thuộc tính
# #
tb_name = input('---- Enter name of Table : ').upper()

#
# phần này để lấy tên các thuộc tính trong bảng
# sử dụng lệnh SP_COLUMNS tui thấy tên các thuộc tinhs ở côth thứ 3
# như này : ('QLSV', 'dbo', 'MonHoc', 'MaMH',.....)
# #
cursor.execute('SP_COLUMNS '+tb_name+'')

list_columns = []

for row in cursor:
    list_columns.append(row[3])

print('number of columns will be added : ' + str(len(list_columns)))
print('Attributes will be added : ', end='')
print(list_columns)

#
# đoạn quan trọng này dung .execute để  nhập lệnh INSERT INTO table (...) VALUES (...)
# #

try:
    for row in df.itertuples():
        sql = 'INSERT INTO '+tb_name + \
            ' ({}) VALUES ({})'.format(
                ','.join(list_columns), ','.join(['?']*len(df.columns)))
        cursor.execute(sql, tuple(row[1:]))
    print('add success')
except NameError:
    print(NameError)


cursor.commit()
