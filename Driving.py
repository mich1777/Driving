country = input('請問你是哪國人？')
age = input("請問你幾歲？")
age = int(age)
if country == '台灣':
    if age >= 18:
        print('可考駕照')
    else:
        print('不可以考駕照')
