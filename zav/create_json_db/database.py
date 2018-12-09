def add_worker(db, first_name, second_name, job, age, pay):
    record = dict(name=dict(first=first_name, second=second_name), job=job, age=age, pay=pay)
    db[first_name + '_' + second_name] = record


db = {}
add_worker(db, 'Jamie', 'Oliver', 'cook', 47, 500000)
add_worker(db, 'Bob', 'Tornton', 'actor', 52, 1000000)
add_worker(db, 'Sue', 'Jonson', 'janitor', 47, 10000)

if __name__ == '__main__':
    for key in db:
        print(key, '=> \n ', db[key]['name']['first'] +
              ' ' + db[key]['name']['second'] +
              ', ' + db[key]['job'] +
              ', ' + str(db[key]['age']) +
              ', ' + str(db[key]['pay']))
        input("press any key")


