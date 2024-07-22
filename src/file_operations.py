from os import walk, stat
from os.path import splitext
from .utils import get_path
from .db_operations import execute_query_print

# Walk throughout the file_path, get the required info and insert into table
def insert_files(connection, cursor, file_path, query_insert, table_name):
    for folder, subfolders, files in walk(file_path):
        for file in files:
            file_full_path = get_path(folder, file)
            file_size = stat(file_full_path).st_size
            file_extension = splitext(file)[1]
            execute_query_print(
                connection, cursor, query_insert, (file_full_path, file_size, file_extension), to_print=False
                )
            print(f"({file_full_path}, {file_size}, {file_extension})")
    print()
