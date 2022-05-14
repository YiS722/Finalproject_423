import sqlite3
import pandas as pd


db_connect = sqlite3.connect('RU.db')


#1-How many students are there in total? 5

df = pd.read_sql('SELECT COUNT(*) from Student; ',con=db_connect)

print("1:")
print(df)


#2----Students who did not attend any events? None

sql = """
SELECT * from Student 
where student_id not in (
SELECT student_id from Participation
)
"""
df = pd.read_sql(sql,con=db_connect)
print("2:")
print(df)


#3 --- ---There are those depts that publish more than 2 events ?  Department of Chinese


sql = """
SELECT d.dept_id,d.dept_name,count(*) as event_num
from Department d,Activity e 
WHERE d.dept_id = e.dept_id
GROUP BY d.dept_id,d.dept_name
HAVING COUNT(*) > 2
"""
df = pd.read_sql(sql,con=db_connect)
print("3:")
print(df)


#4 --- How many students does each dept have?


sql ="""
SELECT d.dept_id,d.dept_name,count(*) as student_number
from Department d,Enrollment e,Major m 
WHERE d.dept_id =m.dept_id and e.major_id = m.major_id
GROUP BY d.dept_id,d.dept_name;"""

df = pd.read_sql(sql,con=db_connect)
print("4:")
print(df)


#5 --What kind of students are there in the math department? Ma ,Peter

sql ="""
SELECT d.dept_id,d.dept_name,s.student_id,student_fname,student_lname
from Department d,Enrollment e,Major m ,Student s
WHERE d.dept_id =m.dept_id and e.major_id = m.major_id and s.student_id = e.student_id
and d.dept_name ='Department of Math'"""

df = pd.read_sql(sql,con=db_connect)
print("5:")
print(df)



db_connect.close()