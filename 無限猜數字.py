import random
num=random.randint(1,10)
y=input('請輸入數字')
x=0
while int(y)!=num :
    print('你猜錯了喔，再試試看吧')
    y=input('請再輸入數字')
else:
    print('太厲害了')

   
