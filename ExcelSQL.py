import pandas as pd
from sqlalchemy import create_engine
svr_name = 'localhost'
db_name = 'MNG'
u_name = 'sa'
u_pass = '123456aA@$'
# Id and password should be read with a secure way
your_data_frame = pd.read_excel('student.xlsx')
# your_data_frame = pd . read_csv ( " CSV_Delhi_fight_details.csv " )
eng = create_engine ( " mssql + pyodbc : // " + u_name + " : " + u_pass + " @ " + svr_name + " / db_pandas_class ? driver = SQL + Server " )