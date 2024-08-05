import sqlite3

DATABASE = 'Student_Database.db'


# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect(DATABASE)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Read the schema from the schema.sql file and execute it
with open('MyMark_Schema.sql', 'r') as schema_file:
    schema = schema_file.read()
    cursor.execute(schema)

print("Table is created")

# cursor.execute("INSERT OR IGNORE INTO authentication (username, password, city, SchoolName, PostalCode, DateOfBirth) \
#                VALUES ('123456', 'password123', 'Burnaby', 'Burnaby South', 'V5K 282', '2010-10-13')")

cursor.execute("INSERT OR IGNORE INTO StudentMarks (username, subject, grade) VALUES ('123456', 'Math', 'A')")


# Commit the changes and close the connection
conn.commit()
conn.close()