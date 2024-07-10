import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '96321'
)
#Prepare a cursor object
cursorObject = database.cursor()

# Create Database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")