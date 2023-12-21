from connect import *

c.execute('''
          CREATE TABLE IF NOT EXISTS menuItems
          (id INTEGER PRIMARY KEY, name TEXT, price INT, type TEXT)
          ''')

conn.commit()