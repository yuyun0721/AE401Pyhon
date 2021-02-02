x=input('請輸入數學成績')
y=input('請輸入英文成績')
if int(x)>89 and int(y)>89:
    print('good!')
elif int(x)>59 and int(y)<59:
    print('還不錯')
else:
    print('加油')
