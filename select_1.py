import sqlite3

DATABASE = 'Student_Database.db'


# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect(DATABASE)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

info = cursor.execute("SELECT * FROM StudentMarks");
  
# for row in info:  
#    print ("username = ", row[0])  
#    print ("password = ", row[1])  
#    print ("city = ", row[2])
#    print ("SchoolName = ", row[3])
#    print ("PostalCode = ", row[4])
#    print ("DateOfBirth = ", row[5], "\n")

for row in info:  
   print ("username = ", row[0])  
   print ("password = ", row[1])  
   print ("grade = ", row[2], "\n")
