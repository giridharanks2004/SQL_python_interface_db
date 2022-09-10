from http import server
from lib2to3.pygram import Symbols
from random import randint
from sqlite3 import Cursor
from sys import implementation
from tabnanny import check
from turtle import goto
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
                cursor.execute('select * from userinfo;')
                check2=cursor.fetchall()
                for i in check2:
                    if inp2==i[1]:
                       import random
                       alphalower='abcdefghijklmnopqrstxyz'
                       alphaupper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                       numer='0123456789'
                       symbols='<>?:!@#$%^&*()'
                       capt_size=6
                       captcha=alphalower+alphaupper+numer+symbols
                       passwd="".join(random.sample(captcha,capt_size))
                       print('captcha=',passwd)
                       captch=input('enter captcha:')
                       if passwd==captch:
                          print('login succesful')
                          cursor.execute("select * from userinfo where uid='{}';".format(inp1))
                          user_info=cursor.fetchall()
                          for i in user_info:
                              print('name:',i[0])
                              print('password:',i[1])
                       else:
                          print('human verification failed!')
                          break
    elif ch1==2:
        inpun=input('enter valid user name:')
        cursor.execute('select * from userinfo;')
        checknameavial=cursor.fetchall()
        for i in checknameavial:
            if inpun==i[0]:
                print('enter unique username!!!')
                inpun=input('enter unique user name:')
                if inpun!=i[0]:
                    inpwd=input("enter valid password:")
                    if inpwd==i[1]:
                        print('enter unique password')
                        inpwd=input("enter valid password:")
                        if inpwd!=i[1]:
                            inpmail=input('enter mail id to register:')
                            if inpmail==i[3]:
                                print('enter unique email id!')
                                inpmail=input('enter mail id to register:')
                                if inpmail!=i[3]:
                                    cursor.execute("use vodpass;")
                                    cursor.execute("insert into userinfo values('{}','{}','{}');".format(inpun,inpwd,inpmail))
                                    curs.commit()
                                    print('the user info has been added sign in to continue')
    cho=input('do you want sign in again? y/n:')