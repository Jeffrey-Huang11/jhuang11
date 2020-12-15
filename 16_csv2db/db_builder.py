# Team Elephant (Jeffrey Huang, Matthew Hui, Winnie Huang, Ethan Machleder)
# SoftDev
# K16 -- No Trouble
# 2020-12-16

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
print("sucessfully connected to sqlite")

#==========================================================

# CODE TO POPULATE THE course_grades db CONTAINING courses.csv DATA

c.execute('DROP TABLE IF EXISTS course_grades')
c.execute('''CREATE TABLE "course_grades"(
	"name" TEXT,
	"grade" INTEGER,
	 "id" INTEGER)
	 ''')
with open('courses.csv') as csvfile:
	myCSVReader = csv.DictReader(csvfile)
	for row in myCSVReader:
		name_a = row.get("code")
		grade_a = row.get("mark")
		identifier = row.get("id")
		c.execute("INSERT INTO course_grades (name, grade, id) VALUES (?, ?, ?)",
          (name_a, grade_a, identifier))

#print the course_grades SQLite table
command = "SELECT * FROM course_grades;"
print("\n course_grades: \n")
for row in c.execute(command):
    print(row)
db.commit() #save changes
print("Record inserted successfully into SqliteDb_developers table ")

#==========================================================

# CODE TO POPULATE THE student_data DB FROM THE students.csv FILE

c.execute('DROP TABLE IF EXISTS student_data')
c.execute('''CREATE TABLE "student_data"(
	"name" TEXT,
	"age" INTEGER,
	 "id" INTEGER)
	 ''')
with open('students.csv') as csvfile:
	myCSVReader = csv.DictReader(csvfile)
	for row in myCSVReader:
		name_a = row.get("name")
		age_a = row.get("age")
		identifier = row.get("id")
		c.execute("INSERT INTO student_data (name, age, id) VALUES (?, ?, ?)",
          (name_a, age_a, identifier))

#print the student_data SQLite table
command = "SELECT * FROM student_data;"
print(" \n student_data: \n")
for row in c.execute(command):
    print(row)
db.commit() #save changes
print("Record inserted successfully into SqliteDb_students table ")

#==========================================================

db.close()  #close database
