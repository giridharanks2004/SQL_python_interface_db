from ast import Or
import mysql.connector as m
curs2=m.connect(host="localhost",user='root',passwd="3000")
cursor2=curs2.cursor()
while curs2.is_connected:
    #cursor2.execute("create database adminpas")
    cursor2.execute("use adminpas;")
    #cursor2.execute("create table admininfo(aid varchar(10),paswd varchar(10));")
    curs2.commit()
    break
cho2="y"
while cho2=='y': 
    print ("-----ADMIN LOGIN STREAM-DATABASE HBO MAX---------")
    print('1.Admin Login') 
    ch1=int(input("enter your choice to proceed:"))
    if ch1==1:
        inp101=input("enter you admin id:")
        cursor2.execute('select * from admininfo;')
        check=cursor2.fetchall()
        for i in check:
            if inp101==i[0]:
                print("admin id found")
                inp202=input("enter your password:")
                if inp202==i[1]:
                    print('login sucessfull!')
                    cho3=int(input('''select your choice to manuipulate USERINFO Database
                                                   1.VIEW LOGGED USERS
                                                   2.SEARCH LOGGED USERS
                                                   3.REVOKE USER PERMISSON
                                                   select your option:'''))
                    if cho3==1:
                        cursor2.execute("use vodpass;")
                        cursor2.execute("select * from userinfo;")
                        uinfo=cursor2.fetchall()
                        for i in uinfo:
                            print(i, 'user currently logged in!')
    cho2=input('do you want to exit the portal:')
    break
                        
                        
                        
                    
                
                
                
