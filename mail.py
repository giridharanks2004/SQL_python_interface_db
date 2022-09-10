from random import randint
import smtplib
code=randint(1000,9999)
msg='your verification code:',code
server=smtplib.SMTP('smtp.google.com',587)
server.starttls
server.login('serverdbdemo01@gmail.com','ksgksg1947')
server.sendmail('serverdbdemo01@gmail.com','iamgiridharanks@gmail.com',msg)
inpmail=input('enter mail:')