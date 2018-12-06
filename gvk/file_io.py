import pprint


def store_raw_db(db, db_file_name):
    db_file = open(db_file_name, 'w')
    pprint.pprint(db, db_file)
    db_file.close()


def read_raw_db(db_file_name):
    db_file = open(db_file_name, 'r')
    db = eval(db_file.read())
    return db
