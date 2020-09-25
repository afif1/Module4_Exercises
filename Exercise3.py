from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///database/Chinook.sqlite')

df = pd.read_sql_query("select * from Employee where EmployeeId >= 6 order by BirthDate", engine)
pd.set_option('display.max_columns', None) #to display all columns

print(df)