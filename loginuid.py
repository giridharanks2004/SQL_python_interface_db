from sqlite3 import Cursor
from tabnanny import check
import mysql.connector as m
curs=m.connect(host="localhost",user='root',passwd="3000")
cursor=curs.cursor()
while curs.is_connected:
    #cursor.execute("create database vodpass")
    cursor.execute("use vodpass;")
    #cursor.execute("create table userinfo(uid varchar(10),paswd varchar(10));")
    curs.commit()
    break
cho="y"
while cho=='y': 
    print ("-----LOGIN/CREATE USER STREAM-DATABASE HBO MAX---------")
    print("1.LOGIN")
    print("2.CREATE USER ID")
    ch1=int(input("enter your choice to proceed:"))
    if ch1==1:
        inp1=input("enter you user id:")
        cursor.execute('select * from userinfo;')
        check=cursor.fetchall()
        for i in check:
            if inp1==i[0]:
                print("user id found")
                inp2=input("enter your password:")
                if inp2==i[1]:
                    print('login sucessfull!')
                else:
                    print('enter correct pwd!')
            else:
                print('user info not found')
    elif ch1==2:
        inpun=input('enter valid user name:')
        inpwd=input("enter valid password:")
        if isinstance(inpun,str):
            cursor.execute("insert into userinfo values('{}','{}');".format(inpun,inpwd))
            curs.commit()
            print('the user info has been added sign in to continue')
        else:
            print("enter proper uid and password to sign up!")
    cho=input('do you want sign in again? y/n:')