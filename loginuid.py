from sqlite3 import Cursor
import mysql.connector as m
curs=m.connect(host="localhost",user='root',passwd="3000")
cursor=curs.cursor()
while curs.is_connected:
    cursor.execute("create database vodpass")
    cursor.execute("use vodpass;")
    cursor.execute("create table userinfo(uid varchar(10),paswd varchar(10));")
    