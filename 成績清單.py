scores=[]
a=0
c=100
n=0
x=int(input('請問班上有幾位同學?'))
for i in range(x):
    y=int(input('請輸入分數:'))
    scores.append(y)
    print(scores)
    n=n+y
    if y>a:     
        a=y
    if y<c:
        c=y
print(a,c)
        
e=n/x
print(e)
