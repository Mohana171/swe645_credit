import mysql.connector

conn = mysql.connector.connect(
    host='swe645-db.c1mkcyic05mk.us-east-1.rds.amazonaws.com',
    user='admin',
    password='YourPassword123!',
    database='swe645'   # <-- update this to match your real DB
)

cursor = conn.cursor()
