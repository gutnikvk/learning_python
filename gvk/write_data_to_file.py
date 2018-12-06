import file_io
import json

bob = {
    'name': 'Bob Smith',
    'age': 42,
    'job': 'dev',
    'pay': 70000
}

sue = {
    'name': 'Sue Jones',
    'age': 45,
    'job': 'teamlead',
    'pay': 150000
}

tom = {
    'name': 'Tom',
    'age': 18,
    'job': None,
    'pay': 0
}

db = {
    'Bob': bob,
    'Sue': sue,
    'Tom': tom
}

print(db)
print(type(json.dumps(db)))  #Convert dictionary to JSON string

db_file_name = 'people_file'

file_io.store_raw_db(db, db_file_name)

input()
