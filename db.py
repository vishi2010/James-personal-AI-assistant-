import csv
import sqlite3

# # Connect to the database (creates jarvis.db if it doesn't exist)
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# # query = "INSERT INTO sys_command VALUES (null, '', '')" # cursor.execute(query) # con.commit()

# # Create the contacts table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS contacts (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(200),
#     mobile_no VARCHAR(255),
#     email VARCHAR(255) NULL
# )
# ''')

# Save changes and close
# con.commit()
# con.close()

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
desired_columns_indices = [0, 3]

# Read data from CSV and insert into SQLite table for the desired columns
with open("contacts.csv", "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        selected_data = [row[i] for i in desired_columns_indices]
        cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
con.commit()
con.close()


# the following lines of code are for inserting single contacts without have to do the whole process. 
# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890' "null")"
# cursor.execute(query)
# con.commit()


# query = 'kunal'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])
