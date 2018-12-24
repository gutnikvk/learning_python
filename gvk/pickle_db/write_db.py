import pickle
from gvk.pickle_db.initdata import bob, sue, tom

db = {
    'Bob': bob,
    'Sue': sue,
    'Tom': tom
}

dbfile = open('people_pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()