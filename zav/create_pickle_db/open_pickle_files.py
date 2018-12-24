import pickle
import glob

for filename in glob.glob('pickled_recs/*.pkl'):  # для ‘bob’,’sue’,’tom’
    rec_file = open(filename, 'rb')
    record = pickle.load(rec_file)
    print(filename, '=>\n ', record)

sue_file = open('pickled_recs/Sue.pkl', 'rb')
print('\n', pickle.load(sue_file)['name'])  # извлечь имя Сью

