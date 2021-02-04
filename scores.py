
scores=[]
x=int(input('請輸入學生人數'))
b=0
c=100

for i in range(x):
    n=str(input('名字'))
    a=int(input('年齡'))
    s=int(input('成績'))
    x=[]
    x.append(n)
    x.append(a)
    x.append(s)
    scores.append(x) 
    if s>b:     
       b=s
    if s<c:
        c=s
print(scores)
b_num=score.index(b)
c_num=score.index(c)
print('最高分是'scores[b_num][0],scores[b_num][2]'分')
print('最低分是'scores[c_num][0],scores[c_num][2]'分')
