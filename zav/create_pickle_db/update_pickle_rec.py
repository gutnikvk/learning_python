import pickle
import os

os.chdir('pickled_recs')

sue_file = open('Sue.pkl', 'rb')
sue = pickle.load(sue_file)
sue_file.close()
sue['pay'] *= 1.10
sue_file = open('Sue.pkl', 'wb')
pickle.dump(sue, sue_file)
sue_file.close()

kek_file = open('Kek.pkl', 'rb')
kek = pickle.load(kek_file)
kek_file.close()
kek['age'] = 20
kek_file = open('Kek.pkl', 'wb')
pickle.dump(kek, kek_file)
kek_file.close()


