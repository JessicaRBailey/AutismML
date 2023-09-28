<!DOCTYPE html>
<html>

<head>
    <title>CSV to SQLite Database Converter</title>
</head>

<body>
    <h1>CSV to SQLite Database Converter</h1>
    <p>This Python script is designed to import data from a CSV file into an SQLite database and retrieve and display
        the data from the database. It uses the Pandas library for data manipulation and Matplotlib for data
        visualization.</p>

    <h2>Usage</h2>
    <ol>
        <li><strong>Requirements</strong>
            <ul>
                <li>Python 3.x</li>
                <li>Required Python packages (install using <code>pip install package_name</code>):
                    <ul>
                        <li><code>sqlite3</code>: To work with SQLite databases.</li>
                        <li><code>pandas</code>: For data manipulation and retrieval.</li>
                        <li><code>matplotlib</code>: For data visualization (commented out but can be uncommented for
                            use).</li>
                    </ul>
                </li>
            </ul>
        </li>

        <li><strong>Configuration</strong>
            <ul>
                <li>Ensure that your SQLite database file name is set as <code>SQLITE.db</code>. You can change this
                    name in the <code>database_name</code> variable if needed.</li>
                <li>Make sure the CSV file you want to import is located within the "Resources" folder. You can change
                    the file path in the <code>csv_file_path</code> variable if necessary.</li>
            </ul>
        </li>

        <li><strong>Run the Script</strong>
            <p>Execute the script by running the following command in your terminal or command prompt:</p>
            <pre><code>python script_name.py</code></pre>
            <p>Replace <code>script_name.py</code> with the actual name of your script.</p>
        </li>

        <li><strong>Data Import</strong>
            <ul>
                <li>The script creates an SQLite database if it doesn't exist and creates a table with specified columns
                    to store the data.</li>
                <li
