import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('path_to_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Run the SQL query
query = "SELECT ID, Name, Population FROM City ORDER BY Population DESC LIMIT 1000"
cursor.execute(query)

# Read the result returned from the database engine
result = cursor.fetchall()

# Print the result
for row in result:
    print(row)

# Close the cursor and the connection to the database
cursor.close()
conn.close()