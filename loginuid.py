from random import randint
from sqlite3 import Cursor
from sys import implementation
from tabnanny import check
import time
import sys
import mysql.connector as m
done = 'false'
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
                    capt=randint(100001,999998)
                    print('enter the captcha for human verification',capt)
                    captch=int(input('verify:'))
                    if capt==captch:
                        print('login succesful')
                    else:
                        print('human verification failed!')
                else:
                    print('enter correct pwd!')
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