def get_queries(table_name):

  query_create_table = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
    FileID INTEGER PRIMARY KEY AUTOINCREMENT,
    FilePath VARCHAR(255) NOT NULL,
    FileSize BIGINT NOT NULL,
    FileExtension VARCHAR(10) NOT NULL -- Alternatively, INT if it is smaller
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
