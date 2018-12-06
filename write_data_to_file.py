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

input()