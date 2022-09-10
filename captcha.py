import random
alphalower='abcdefghijklmnopqrstxyz'
alphaupper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numer='0123456789'
symbols='<>?:!@#$%^&*()'
capt_size=5
captcha=alphalower+alphaupper+numer+symbols
passwd="".join(random.sample(captcha,capt_size))
print('captcha=',passwd)