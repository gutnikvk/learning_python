import gvk.file_io as file_io

db = file_io.read_raw_db('people_file')
print(db['Bob'])
print(db)
