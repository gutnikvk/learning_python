from database import db
import pickle


def store_pickle_db(database, db_file_name):
    db_file = open(db_file_name, 'wb')
    print(pickle.dump(database, db_file))
    db_file.close()


store_pickle_db(db, 'people_pickle')
