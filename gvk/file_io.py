ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def store_database(db, db_file_name):
    db_file = open(db_file_name, 'w')
    for key in db:
        print(key, file=db_file)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=db_file)
        print(ENDREC, file=db_file)
    print(ENDDB, file=db_file)
    db_file.close()


def read_database(db_file_name):
    db_file = open(db_file_name)
    import sys
    sys.stdin = db_file
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db