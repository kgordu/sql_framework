from sqlite3 import Error

from config.constants import (
  DB_NAME, DB_FOLDER, FILE_EXTENSION,
  FILE_FOLDER_NAME, TABLE_NAME, MAX_NUMBER
)

from src.db_operations import create_connection, execute_query_print, print_tables
from src.file_operations import insert_files
from src.queries import get_queries
from src.utils import get_path

def main():
    db_name = DB_NAME
    db_folder = DB_FOLDER
    file_extension = FILE_EXTENSION
    file_folder_name = FILE_FOLDER_NAME
    table_name = TABLE_NAME
    max_number = MAX_NUMBER

    my_db_path = get_path(db_folder, db_name)
    my_files_path = get_path(file_folder_name)
    my_connection, my_cursor = create_connection(my_db_path)
    my_queries = get_queries(table_name)


    try:
        # Create a table
        print(f"Table '{table_name}' is created.")
        execute_query_print(my_connection, my_cursor, my_queries['create_table'])
        print("Current tables are:")
        print_tables(my_cursor)

        # Insert the files in the given directory and get the inserted rows
        print("Current rows are:")
        insert_files(my_connection, my_cursor, my_files_path, my_queries['insert'], table_name)

        # Get n Largest Files
        print(f"Largest {max_number} Files:")
        execute_query_print(my_connection, my_cursor, my_queries['get_n_largest_files'], (max_number,))

        # Print files with .txt extension
        print(f"Files with '{file_extension}' extension:")
        execute_query_print(my_connection, my_cursor, my_queries['file_extension'], (file_extension,))

    except Error as e:
        print(f"Error during execution: {e} in main program.\n")

    finally:
        #Finally, close the connection if it is still open
        if my_connection:
            my_connection.close()

if __name__ == '__main__':
    main()
