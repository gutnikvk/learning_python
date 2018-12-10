import pickle

db_file = open('people_pickle', 'rb')
db = pickle.load(db_file)
db_file.close()

db['Sue']['pay'] *= 1.2
db['Tom']['job'] = 'sex-slave'

db_file = open('people_pickle', 'wb')
pickle.dump(db, db_file)
db_file.close()
