# SQLite3 Framework

## Overview

**SQLite3 Framework** is a Python-based application designed to interact with an SQLite database. It includes functionalities for creating tables, inserting file data, querying for specific file details, and more. The application provides a comprehensive way to manage and query file information within a database.

## Features

- **Database Management:** Create and manage tables within an SQLite database.
- **File Insertion:** Insert file details (path, size, extension) into the database.
- **File Querying:** Retrieve file information based on size or extension.
- **Dynamic Path Handling:** Automatically determine file paths relative to the project directory.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/sql_framework.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd sql_framework
    ```

3. **Install any required dependencies (if applicable).**
    ```bash
    pip install -r requirements.txt
    ```

## Usage  

1. Ensure you have Python 3.x installed.

2. Run the application by executing:
    ```bash
    python main.py
    ```

3. Follow the on-screen prompts to interact with the database, manage file information, and execute queries.

## Project Structure

```markdown
📁 project-root
├── 📁 config
│ ├── 📄 __init__.py
│ └── 📄 constants.py
│
├── 📁 src
│ ├── 📄 __init__.py
│ ├── 📄 db_operations.py
│ ├── 📄 queries.py
│ └── 📄 utiles.py
│
├── 📄 .gitignore
├── 📄 .gitattributes
└── 📄 main.py
```


* **config/**: Contains configuration files.
  * ***\__init__.py***: Imports constants for database configuration.
  * ***constants.py***: Defines constants used throughout the database.

* **src/**: Contains source code files.
  * ***\__init__.py***: Initializes the source package and sets up logging.
  * ***db_operations.py***: Functions for file handling and insertion into the database.
  * ***queries.py***: Provides SQL queries for table creation, insertion, and retrieval.
  * ***utils.py***: Utility functions for path handling.

* **.gitignore**: Specifies files and directories to be ignored by Git (e.g., virtual environments, build artifacts).

* **.gitattributes**: Ensures consistent line endings across different operating systems in the repository.

* **main.py**: The entry point of the application. Initializes settings, handles database operations, and manages file interactions.

## Code Examples

### Database Operations

#### Create Connection
```python
from sqlite3 import Error, connect
from os import makedirs
from os.path import dirname

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
```

#### Execute Queries:
 ```python
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

 ```

 #### File Operations:
 * Insert Files:
 ```python
from os import walk, stat
from os.path import splitext
from .utils import get_path
from .db_operations import execute_query_print

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

 ```

 #### Queries
 * Get Queries:
 ```python
def get_queries(table_name):
    query_create_table = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
    FileID INTEGER PRIMARY KEY AUTOINCREMENT,
    FilePath VARCHAR(255) NOT NULL,
    FileSize BIGINT NOT NULL,
    FileExtension VARCHAR(10) NOT NULL
    );
    """

    query_insert = f"INSERT INTO {table_name} (FilePath, FileSize, FileExtension) VALUES (?, ?, ?)"

    query_get_n_largest_files = f"""
    SELECT * FROM {table_name}
    ORDER BY FileSize DESC
    LIMIT ?
    """

    query_file_extension = f"""
    SELECT * FROM {table_name}
    WHERE FileExtension=?
    ORDER BY FileID DESC
    """

    return {
        'create_table': query_create_table,
        'insert': query_insert,
        'get_n_largest_files': query_get_n_largest_files,
        'file_extension': query_file_extension,
    }

 ```

#### Utility Functions
* Get Path:
```python
from os.path import dirname, join, abspath

def get_path(folder_name, file_name=None):
    current_path = dirname(abspath(__file__))
    project_path = dirname(current_path)
    if file_name:
        full_path = join(project_path, folder_name, file_name)
    else:
        full_path = join(project_path, folder_name)
    return full_path

```

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](https://github.com/kivanc57/sql_framework/blob/main/LICENSE) file for details.


## Contact
Let me know if there are any specific details you’d like to adjust or additional sections you want to include!  
* **Email**: kivancgordu@hotmail.com
* **Version**: 1.0.0
* **Date**: 22-06-2024
