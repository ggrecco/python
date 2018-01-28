from dml import db_delete, db_insert, db_select, db_update
from pprint import pprint
'''
db_insert('vvert', '11111111', 'vvert@riot.com')
db_insert('4Lan', '11111111', '4Lan@riot.com')
db_insert('kami', '11111111', 'kami@riot.com')
db_insert('esa', '11111111', 'esa@riot.com')
db_insert('dioud', '11111111', 'dioud@riot.com')
'''
pprint(db_select('11111111','phone'))
