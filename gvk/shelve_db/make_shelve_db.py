import shelve
from gvk.shelve_db.initdata import tom, bob, sue

db = shelve.open('shelve_people')
db['Bob'] = bob
db['Tom'] = tom
db['Sue'] = sue
db.close()