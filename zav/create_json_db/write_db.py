import file_io as file_io
from database import db as db

db_file_name = 'json_db.json'

file_io.store_raw_db(db, db_file_name)
