'''
Mykolyk Fan Club: Shafiul Haque, April Li, David Deng
SoftDev  
skeleton/stub :: SQLITE3 BASICS
Oct 26, 2022
Time Spent: 1.5 hr S

DISCO: 
- learnt of fetchall's use for sqlit
- with open(file.csv) as f: 

QCC: 
- since we need to drop tables before running the program again, does it mean that databases cannot be overwritten? 

OPS SUMMARY:
- delete pre exisitng tables
- intializes tables with parameters
- opens csv files and assigns it to the corresponding values on the tables 
- print databases with fetchall 

'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#deletes table if preexisting (does this mean that databases cannot be overwritten?)
db.execute("DROP TABLE if exists courses") 
db.execute("DROP TABLE if exists students")
#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
#initializes table with parameters
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")
c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")

#opens csv files for parsing       
with open('courses.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        c.execute(f"""INSERT INTO courses
                    VALUES("{row['code']}", {row['mark']}, {row['id']})
                """)

with open('students.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        c.execute(f"""INSERT INTO students
                    VALUES("{row['name']}", {row['age']}, {row['id']})
                """)

#saves tables into database
db.commit() #save changes

#prints database info!
print("STUDENT DATABASE\n")
c.execute("SELECT * FROM STUDENTS")
print(c.fetchall())

print("\nCOURSE DATABASE\n")
c.execute("SELECT * FROM COURSES")
print(c.fetchall())
db.close()
#==========================================================


