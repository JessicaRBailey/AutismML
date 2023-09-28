CSV to SQLite Database Converter
This Python script is designed to import data from a CSV file into an SQLite database and retrieve and display the data from the database. It uses the Pandas library for data manipulation and Matplotlib for data visualization.

Usage
Requirements

Python 3.x
Required Python packages (install using pip install package_name):
sqlite3: To work with SQLite databases.
pandas: For data manipulation and retrieval.
matplotlib: For data visualization (commented out but can be uncommented for use).
Configuration

Ensure that your SQLite database file name is set as SQLITE.db. You can change this name in the database_name variable if needed.
Make sure the CSV file you want to import is located within the "Resources" folder. You can change the file path in the csv_file_path variable if necessary.
Run the Script

Execute the script by running the following command in your terminal or command prompt:

bash
Copy code
python script_name.py
Replace script_name.py with the actual name of your script.

Data Import

The script creates an SQLite database if it doesn't exist and creates a table with specified columns to store the data.
It imports data from the CSV file into the SQLite table, skipping the header row.
Data Retrieval and Visualization

The script retrieves data from the SQLite database and displays it in a readable format.
Data visualization using Matplotlib is supported but commented out. Uncomment the appropriate lines to enable data visualization.
Customization
You can customize the script to work with different CSV files by changing the csv_file_path variable and the table structure.
Modify the code for data visualization to suit your specific needs.
License
This script is provided under the MIT License.
