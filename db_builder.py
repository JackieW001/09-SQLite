import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#open csv files
peeps = csv.DictReader(open("peeps.csv"))
peeps_value = []
courses = csv.DictReader(open("courses.csv"))


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

# create peeps table
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER);")
for i in peeps:
    c.execute("INSERT INTO peeps VALUES ( '" +
              i["name"] + "'," +
              i["age"] + "," +
              i["id"] +
              ");")

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")
for i in courses:
    c.execute("INSERT INTO courses VALUES ( '" +
              i["code"] + "'," +
              i["mark"] + "," +
              i["id"] +
              ");")

db.commit() #save changes
db.close()  #close database


