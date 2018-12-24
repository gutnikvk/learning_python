from database import bob, sue, tom, kek
import pickle

for (key, record) in [('Bob', bob), ('Tom', tom), ('Sue', sue), ('Kek', kek)]:
    with open('pickled_recs/' + key + '.pkl', 'wb') as rec_file:
        pickle.dump(record, rec_file)
    rec_file.close()
