bob = {
    'name': {
        'first': 'Bob',
        'second': 'Smith'
    },
    'age': 42,
    'job': 'dev',
    'pay': 70000
}

sue = {
    'name': {
        'first': 'Sue',
        'second': 'Jonson'
    },
    'age': 45,
    'job': 'teamlead',
    'pay': 150000
}

tom = {
    'name': {
        'first': 'Tom',
        'second': '???'
    },
    'age': 18,
    'job': None,
    'pay': 0
}

kek = {
    'name': {
        'first': 'kek',
        'second': 'lel'
    },
    'age': 18,
    'job': None,
    'pay': 0
}

db = {
    'Bob': bob,
    'Sue': sue,
    'Tom': tom,
    'Kek': kek
}


if __name__ == '__main__':
    for key in db:
        print(key, '=> \n ', db[key]['name']['first'] +
              ' ' + db[key]['name']['second'] +
              ', ' + str(db[key]['job']) +
              ', ' + str(db[key]['age']) +
              ', ' + str(db[key]['pay']))



