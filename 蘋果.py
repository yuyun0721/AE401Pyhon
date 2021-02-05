y={'g':0,
   'l':0,
   'm':0}

k=[]
x1=0
t1=0
d1=0
d2=0
u=y['l']*y['m']

while True:
    
    print('功能有:')
    print('1.設定')     
    print('2.進貨')
    print('3.出貨')
    print('4.營業額總計')
    print('5.庫存統計')
    print('6.離開系統')

    a=int(input('請輸入您需要的功能'))
    if (a==1):
        x=int(input('請問一共有多少顆蘋果?'))
        x1=int(input('請問一顆蘋果多少錢?'))
        print('一共',x,'顆蘋果')
        print('一顆',x1,'塊錢')
        y['g']=x
        y['l']=x1
        
    elif(a==2):
        t=int(input('請問要進貨多少顆蘋果?'))
        t1=y['g']+t
        print('一共進貨',t,'顆蘋果')
        print('現在共有',t1,'顆蘋果')
        y['g']=t1
        
    elif (a==3):
        d=int(input('請問賣出多少顆蘋果?'))
        d1=d*x1
        d2=y['g']-d
        print('一共賣出',d,'顆蘋果')
        print('應收',d1,'塊錢')
        print('現在共剩下',d2,'顆蘋果')
        r=[]
        r.append(d)
        r.append(d1)
        r.append(d2)
        k.append(r)
        y['g']=d2
        y['m']=d
         
    elif (a==4):
        print('今天有',len(k),'筆交易')
        for i in range(len(k)):
            print('第',i+1,'筆交易，賣出',k[i][0],'顆蘋果，',k[i][1],'元')
        print('共賣了',y['m'],'顆')
        print('營業額',y['l']*y['m'],'元')

    elif (a==5):
        print('還有',y['g'],'顆蘋果')

    elif (a==6):
        fo=open('myfile.txt','w')
        x=str(y['g'])
        u=str(y['l']*y['m'])
        fo.write(x)
        fo.write('\n')
        fo.write(u)
        fo.close()
        break

    else:
        print('輸入錯誤，請再試一次')
