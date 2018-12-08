import json

def store_raw_db(db, db_file_name):
    db_file = open(db_file_name, 'w')
    print(json.dumps(db, indent=4), file=db_file)
    db_file.close()


def read_raw_db(db_file_name):
    db_file = open(db_file_name, 'r')
    db = json.loads(db_file.read())
    return db