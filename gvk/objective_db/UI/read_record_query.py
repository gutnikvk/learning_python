import shelve

db = shelve.open('../class_shelve')

while True:
    key = input('\nEnter the key, please => ')
    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "%s"!' % key)
    else:
        print(record.get_full_name() + ',', record.get_age(), '=>', record.get_job() + ',', record.get_pay())