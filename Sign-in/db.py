import hashlib
import sqlite3
from hashlib import blake2b
from sqlite3.dbapi2 import Cursor

def insert_user():
    conn = sqlite3.connect('sigin.db')
    cursor = conn.cursor()

    sql = ''' CREATE TABLE USER (username text, email text, hashed_password text)'''
    cursor.execute(sql)

    hlib = blake2b(key=b'signin1234567845235267')
    hlib.update('abcdef'.encode('utf-8'))
    hash_passcode = hlib.hexdigest()

    sql1 = f''' INSERT INTO USER VALUES ("Joel","email@gmail", "{hash_passcode}")'''
    cursor.execute(sql1)
    conn.commit()

    sql2 = "SELECT * FROM USER"
    cursor.execute(sql2)
    all_items = cursor.fetchall()


    print(all_items)


    conn.close()

insert_user()