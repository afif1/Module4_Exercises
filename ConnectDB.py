from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///database/Chinook.sqlite')

table_names = engine.table_names()
print(table_names)
'''
con = engine.connect()
rs = con.execute("select * from Album")
df = pd.DataFrame(rs.fetchall())
print(df)
'''

'''
with engine.connect() as con:
    rs = con.execute("select LastName,Title from Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns= rs.keys() #assigns dataframe's column names to the corresponding names of the table columns
    print(df)
'''

'''
with engine.connect() as con:
    rs = con.execute("select * from Employee where EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df.head())
'''

with engine.connect() as con:
    rs = con.execute("select * from Employee order by BirthDate")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df.head())


con.close()