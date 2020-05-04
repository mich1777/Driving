import os
country = input('請問你是哪國人？')
if country != '台灣' and '美國':
    os._exit(0) 
age = input("請問你幾歲？")
age = int(age)
if country == '台灣':
    if age >= 18:
        print('可考駕照')
    else:
        print('不可以考駕照')
elif country == '美國':
    if age >= 16:
        print('可考駕照')
    else:
        print('不可以考駕照')