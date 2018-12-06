import file_io

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

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])

db_file_name = 'people_file.txt'

file_io.store_database(db, db_file_name)
input()
