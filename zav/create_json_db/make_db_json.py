import json_io as file_io
from database import db as db

file_io.store_json_db(db, 'json_db.json')
