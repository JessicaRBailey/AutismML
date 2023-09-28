
import sqlite3
import csv
import os
import pandas as pd

# Define the name of your SQLite database file with the full path.
database_name = os.path.join("Resources", "SQLITE.db")

# Define the path to the CSV file located within the "Resources" folder.
csv_file_path = os.path.join("Resources", "Toddler Autism dataset July 2018.csv")

# Create a SQLite database connection.
conn = sqlite3.connect(database_name)

# Create a cursor object to execute SQL commands.
cursor = conn.cursor()

# Define the name of the table you want to create in the database.
table_name = "sample"

# Create the table in the database if it doesn't exist with the provided columns.
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        Case_No INTEGER,
        A1 INTEGER,
        A2 INTEGER,
        A3 INTEGER,
        A4 INTEGER,
        A5 INTEGER,
        A6 INTEGER,
        A7 INTEGER,
        A8 INTEGER,
        A9 INTEGER,
        A10 INTEGER,
        Age_Mons INTEGER,
        Qchat_10_Score INTEGER,
        Sex TEXT,
        Ethnicity TEXT,
        Jaundice TEXT,
        Family_mem_with_ASD TEXT,
        Who_completed_the_test TEXT,
        Class_ASD_Traits TEXT
    );
''')

# Open the CSV file and insert its data into the SQLite table.
with open(csv_file_path, "r") as file:
    csv_reader = csv.reader(file)
    # Skip the header row if it exists.
    next(csv_reader, None)
    for row in csv_reader:
        cursor.execute(f'''
            INSERT INTO {table_name} (
                Case_No, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, 
                Age_Mons, Qchat_10_Score, Sex, Ethnicity, Jaundice, 
                Family_mem_with_ASD, Who_completed_the_test, Class_ASD_Traits
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', row)

# Commit the changes and close the connection.
conn.commit()
conn.close()

# print(f"Data from {csv_file_path} has been imported into {database_name}.")
#################################################################################

# Define the name of your SQLite database file.
database_name = os.path.join("Resources", "SQLITE.db")

# Create a SQLite database connection.
conn = sqlite3.connect(database_name)

# Create a cursor object to execute SQL commands.
cursor = conn.cursor()

# Define the name of the table you want to query.
table_name = "sample"

# Execute an SQL query to select all rows from the table.
cursor.execute(f"SELECT * FROM {table_name}")

# Fetch all the rows as a list of tuples.
rows = cursor.fetchall()

# Close the connection.
conn.close()

# Display the data in a readable format.
for row in rows:
    print(row)


##################################################################################


# Define the name of your SQLite database file.
database_name = os.path.join("Resources", "SQLITE.db")

# Create a SQLite database connection.
conn = sqlite3.connect(database_name)

# Define the name of the table you want to query.
table_name = "sample"

# Use Pandas to read the table data into a DataFrame.
df_01 = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

# Close the database connection.
conn.close()

# Display the DataFrame.
print(df_01)



