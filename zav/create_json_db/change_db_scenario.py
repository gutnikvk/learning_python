import json
from json_io import store_json_db

with open('json_db.json') as json_data:
    db = json.load(json_data)
    print(db)
    db['Sue_Simone']['pay'] *= 1.10
    db['Bob_Thornton']['name']['first'] = 'Tom Tom'
    store_json_db(db, 'json_db.json')
input()
