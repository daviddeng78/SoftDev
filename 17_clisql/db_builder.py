#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

db.execute("DROP TABLE if exists courses")
#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")
        
with open('courses.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        c.execute(f"""INSERT INTO courses
                    VALUES("{row['code']}", {row['mark']}, {row['id']})
                """)

db.commit() #save changes

# c.execute(f""".open discobandit.db""")
# c.execute("SELECT * from courses")
db.close()
#==========================================================


