import pickle

dbfile = open('people_pickle', 'rb')
db = pickle.load(dbfile)
print(db)
dbfile.close()