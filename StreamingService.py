import mysql.connector as m
cur=m.connect(host="localhost",user="root",passwd="3000")
#cur = m.connect(user='root', password='root', host='127.0.0.1', auth_plugin='mysql_native_password')
cursor=cur.cursor()
while cur.is_connected:
    #cursor.execute("create database vodlibgiri;")
    cursor.execute("use vodlibgiri;")
    #cursor.execute("create table originalproductions(Sno int,content_name varchar(40),production_year int(4),budget int,release_year int(4))")
    #cursor.execute("create table licensed_content(content_name varchar(40),license_price int)")
    #cursor.execute("create table CONTENT_ACQUIREMENT(content_name varchar(40),prod_house varchar(30),price int)")
    #cur.commit()
    break
choicenter='y'
while choicenter == 'y':
    print("----------WELCOME TO HBOMAX STREAMDATABASE-----------")
    print("**********a WARNERMEDIA company************")
    print("1.ORIGINAL PRODUCIONS")
    print("2.LICENSED CONTENT")
    print("3.CONTENT PURCHASED")
    ch=int(input("ENTER YOU CHOICE"))
    if ch ==1:
        print("WELCOME TO ORIGINAL PRODUCTIONS")
        choice1=int(input('''
        You have selected the ORIGNIAL PRODUCTIONS table
        What would you like to do : 
         1. View
         2. Add
         3. Update
         4. Delete
         ENTER YOUR SELECTION:'''))
        if choice1==1:
            print("YOU ARE VIEWING THE RECORDS OF ORIGNAL PRODUCTIONS")
            cursor.execute("select * from originalproductions")
            orgplist=cursor.fetchall()
            print(orgplist.__len__())
            if orgplist.__len__() > 0:
                for i in orgplist:
                    print('serialno : ',i[0])
                    print('content name : ', i[1])
                    print(' production year: ', i[2])
                    print(' production budget: ', i[3])
                    print(' release year: ',i[4])
        elif choice1 == 2:
                   print('Inserting Mode')
                   cursor.execute("use vodlibgiri;")
                   addv='y'
                   while addv=='y':
                       org = int(input("enter serial number:"))
                       org2 = input("content name:")
                       org3 = int(input("production year:"))
                       org4 = int(input("production budget:"))
                       org5 = int(input("release year:"))
                       print("***************************")
                       cursor.execute("insert into originalproductions values({},'{}',{},{},{});".format(org,org2,org3,org4,org5))
                       cur.commit()
                       print('Successfully Added')
                       addv= input('Do you want to continue adding [y]: ').lower()
                       print("***************************")
        elif choice1 == 3:
            print('Updating Mode')
            updatev='y'
            while updatev=='y':
                updatec=int(input('''
        What detail do you want to update : 
         1. sno
         2. content name
         3. production year
         4. production budget
         5. release year

        Enter here  : '''))
                if updatec == 1:
                    print('Updating content')
                    change = int(input('Enter the name of the serialno for which you want to change the no: '))
                    cursor.execute('select * from originalproductions;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input('Enter new name : ')
                            cursor.execute("update originalproductions set Sno = {} where Sno = {};".format(newname, change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                    else:
                        print('Enter proper no')
                elif updatec == 2:
                    print('Updating content name')
                    change = input('Enter the name of the content for which you want to change its content name : ')
                    cursor.execute('select * from originalproductions;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input(input('Enter updated year : '))
                            cursor.execute("update originalproductions set content_name = '{}' where content_name = '{}';".format(newname, change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                    else:
                        print('Enter proper name')
                elif updatec == 3:
                    print('Updating content year name')
                    change = input('Enter the year of the content for which you want to change its year : ')
                    cursor.execute('select * from originalproductions;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input(input('Enter updated year : '))
                            cursor.execute(
                                "update originalproductions set production_year = {} where content_name = {};".format(newname,
                                                                                                        change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                        else:
                            print('Enter proper name')
                elif updatec == 4:
                    print('Updating budget')
                    change = input('Enter the budget for which you want to change its budget : ')
                    cursor.execute('select * from originalproductions;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input(input('Enter updated budget: '))
                            cursor.execute(
                                "update originalproductions set budget = {} where budget = {};".format(
                                    newname,
                                    change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                        else:
                            print('Enter proper budget')
                elif updatec == 5:
                    print('Updating releses')
                    change = input('Enter the name of the content for which you want to change its release date : ')
                    cursor.execute('select * from originalproductions;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input(input('Enter updated year : '))
                            cursor.execute(
                                "update originalproductions set release_year = {} where release_year = {};".format(
                                    newname,
                                    change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                        else:
                            print('Enter proper year')
        elif choice1 == 4:
            delete = 'y'
            while delete == 'y':
                print('Deleting Mode')
                delcon = input('Enter the name of the content you want to delete : ')
                cursor.execute('select * from originalproductions;')
                l = cursor.fetchall()
                for i in l:
                    if i[0] == delcon:
                        cursor.execute("delete from originalproductions where content_name = '{}';".format(delcon))
                        cur.commit()
                        print('Successfully Deleted')
                        break
                else:
                    print('Enter proper content name')
                updatev = input('Do you want to continue updating [y]: ').lower()
                print("********************************")
    elif ch == 2:
        print("WELCOME TO LICENSED CONTENTS")
        choice1 = int(input('''
    You have selected licensed_content table
    What would you like to do : 
     1. View
     2. Add
     3. Update
     4. Delete

    Enter here : '''))
        if choice1 == 1:
            print("YOU ARE VIEWING THE RECORDS OF LICENSED CONTENT")
            cursor.execute("select * from licensed_content")
            orgplist = cursor.fetchall()
            print(orgplist.__len__())
            if orgplist.__len__() > 0:
                for i in orgplist:
                    print('content name : ', i[0])
                    print(' price: ', i[1])
        elif choice1 == 2:
            print('Inserting Mode')
            cursor.execute("use vodlibgiri;")
            addv = 'y'
            while addv == 'y':
                org=input("content name:")
                org2=int(input("price:"))
                print("***************************")
                cursor.execute(
                    "insert into licensed_content values('{}',{});".format(org, org2))
                cur.commit()
                print('Successfully Added')
                addv = input('Do you want to continue adding [y]: ').lower()
                print("***************************")
        elif choice1 == 3:
            print('Updating Mode')
            updatev = 'y'
            while updatev == 'y':
                updatec = int(input('''
                What detail do you want to update : 
                 1. content name
                 2. price
                 

                Enter here  : '''))
                if updatec == 1:
                    print('Updating content')
                    change =(input('Enter the name of the content name for which you want to change the name: '))
                    cursor.execute('select * from licensed_content;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input('Enter new name : ')
                            cursor.execute("update licensed_content set content_name = '{}' where content_name= '{}';".format(newname, change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                    else:
                        print('Enter proper no')
                elif updatec == 2:
                    print('Updating price')
                    change = input('Enter the price of the content for which you want to change its content price : ')
                    cursor.execute('select * from licensed_content;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input(input('Enter updated price : '))
                            cursor.execute("update license_price set license_price = '{}' where license_price = '{}';".format(newname, change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                    else:
                        print('Enter proper price')
        elif choice1 == 4:
            delete = 'y'
            while delete == 'y':
                print('Deleting Mode')
                delcon = input('Enter the name of the content you want to delete : ')
                cursor.execute('select * from licensed_content;')
                l = cursor.fetchall()
                for i in l:
                    if i[0] == delcon:
                        cursor.execute("delete from licensed_content where content_name = '{}';".format(delcon))
                        cur.commit()
                        print('Successfully Deleted')
                        break
                else:
                    print('Enter proper content name')
                updatev = input('Do you want to continue updating [y]: ').lower()
                print("********************************")
    elif ch == 3:
        print("WELCOME TO  CONTENT ACQUIREMENT")
        choice1 = int(input('''
       You have selected licensed_content table
       What would you like to do : 
        1. View
        2. Add
        3. Update
        4. Delete

       Enter here : '''))
        if choice1 == 1:
            print("YOU ARE VIEWING THE RECORDS OF LICENSED CONTENT")
            cursor.execute("select * from content_acquirement")
            orgplist = cursor.fetchall()
            print(orgplist.__len__())
            if orgplist.__len__() > 0:
                for i in orgplist:
                    print('content name : ', i[0])
                    print('production house: ', i[1])
                    print('price:', i[2])
        elif choice1 == 2:
            print('Inserting Mode')
            cursor.execute("use vodlibgiri;")
            addv = 'y'
            while addv == 'y':
                org=input("content name:")
                org2=input("prduction house:")
                org3=int(input("price:"))
                print("***************************")
                cursor.execute("insert into content_acquirement values('{}','{}',{});".format(org, org2,org3))
                cur.commit()
                print('Successfully Added')
                addv = input('Do you want to continue adding [y]: ').lower()
                print("***************************")
        elif choice1 == 3:
            print('Updating Mode')
            updatev = 'y'
            while updatev == 'y':
                updatec = int(input('''
                   What detail do you want to update : 
                    1. content name
                    2. price


                   Enter here  : '''))
                if updatec == 1:
                    print('Updating content')
                    change = (input('Enter the name of the content name for which you want to change the name: '))
                    cursor.execute('select * from content_acquirement;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input('Enter new name : ')
                            cursor.execute("update content_acquirement set content_name = '{}' where content_name= '{}';".format(newname, change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                    else:
                        print('Enter proper no')
                elif updatec == 2:
                    print('Updating production house')
                    change = input('Enter the pdh of the content for which you want to change its content pdh : ')
                    cursor.execute('select * from content_acquirement;')
                    l = cursor.fetchall()
                    for i in l:
                        if i[0] == change:
                            newname = input('Enter updated pdh : ')
                            cursor.execute("update content_acquirement set prod_house = {} where prod_house = '{}';".format(newname, change))
                            cur.commit()
                            print()
                            print('Successfully Updated')
                            break
                    else:
                        print('Enter proper price')
        elif choice1 == 4:
            delete = 'y'
            while delete == 'y':
                print('Deleting Mode')
                delcon = input('Enter the name of the content you want to delete : ')
                cursor.execute('select * from content_acquirement;')
                l = cursor.fetchall()
                for i in l:
                    if i[0] == delcon:
                        cursor.execute("delete from content_acquirement where content_name = '{}';".format(delcon))
                        cur.commit()
                        print('Successfully Deleted')
                        break
                else:
                    print('Enter proper content name')
                updatev = input('Do you want to continue updating [y]: ').lower()
                print("********************************")
        else:
           print("acsess denied!!!!")
    choicenter=input("do you want to restart the server [y?]:").lower()

print("*****************HBO MAX A WARNERMEDIA COMPANY******************")

