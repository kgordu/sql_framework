from config.constants import (
  DB_NAME, DB_FOLDER, FILE_EXTENSION,
  FILE_FOLDER_NAME, TABLE_NAME, MAX_NUMBER
)

from src.db_operations import create_connection, execute_query_print, print_tables
from src.file_operations import insert_files
from src.queries import get_queries
from src.utils import get_path
import logging

logging.basicConfig(
  level=logging.INFO,
  filename='src.log',
  filemode='a',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Package is initialized")

__version__ = "1.0.0"
__date__ = "22-07-2024"
__email__ = "kivancgordu@hotmail.com"
__status__ = "production"

__all__ = [
  'create_connection', 'execute_query_print',
  'insert_files', 'get_queries', 'get_path', 'print_tables',
  'DB_NAME', 'DB_FOLDER', 'FILE_EXTENSION',
  'FILE_FOLDER_NAME', 'TABLE_NAME', 'MAX_NUMBER'
  ]
