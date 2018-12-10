from json_io import store_json_db
from database import db as db


def add_worker(database, first_name, second_name, job, age, pay):
    record = dict(name=dict(first=first_name, second=second_name), job=job, age=age, pay=pay)
    database[first_name + '_' + second_name] = record
    return database


add_worker(db, 'Jamie', 'Oliver', 'cook', 47, 500000)
add_worker(db, 'Bob', 'Thornton', 'actor', 52, 1000000)
add_worker(db, 'Sue', 'Simone', 'janitor', 47, 10000)
store_json_db(db, 'database.py')
