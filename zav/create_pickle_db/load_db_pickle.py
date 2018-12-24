import pickle

db_file = open('people_pickle', 'rb')  # в версии 3.X следует использовать
db = pickle.load(db_file)  # двоичный режим работы с файлами
for key in db:
    print(key, '=>\n', db[key])

print(db['Sue']['name'])

