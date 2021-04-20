import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty123",
    database="pythonprogramming"
)

mycursor= mydb.cursor()

#mycursor.execute("CREATE DATABASE pythonprogramming")
"""
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
"""
#mycursor.execute("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255))")

"""
mycursor.execute("SELECT * FROM actors")

myresult=mycursor.fetchcall()

for x in myresult:
    print(x)

"""

#myresult=mycursor.fetchone()
