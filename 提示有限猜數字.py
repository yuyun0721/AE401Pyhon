y=int(input('請輸入最大上限'))
x=int(input('請輸入最小下限'))
import random
num=random.randint(x,y)
a=int(input('請問你想要有幾次機會?'))
c=int(input('請輸入數字'))
for c in range(a):
    if (c==num):
        print('答對了!')
    elif (c>num):
        a=a-1
        print('太大了，小一點，你還有',a,'次機會')
        c=int(input('請再輸入數字'))
    elif (c<num):
       a=a-1
       print('太小了，大一點，你還有次，',a,'機會')
       c=int(input('請再輸入數字'))
    else:
       print('輸入錯誤，請再試一次')
