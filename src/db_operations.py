from sqlite3 import Error, connect
from os import makedirs
from os.path import dirname

#Create the connection and get the cursor with the connection object
def create_connection(db_path):
    connection = None
    cursor = None
    try:
        makedirs(dirname(db_path), exist_ok=True)
        connection = connect(db_path)
        cursor = connection.cursor()
        print("Connection to SQLite DB successful. Cursor has been created.\n")
    except Error as e:
        print(f"An error occurred during creating connection: {e}\n")
    return connection, cursor

#Execute any kind of query with or without the query placeholder
def execute_query_print(connection, cursor, query, params=None, to_print=True):
    try:
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
        connection.commit()
        if to_print:
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            print()
    except Error as e:
        print(f"An error occurred during execution/fetching: {e}\n")

#Print all the tables
def print_tables(cursor):
    cursor.execute("SELECT name from sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    print()
