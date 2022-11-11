import re
a='welcome 123456'
count=[]
string=''
for s in a:
    if s.isalpha():
        string+=s
#print(string)
for x in re.findall('\d', a):
        y = int(x)
        count.append(y)
sm=sum(count)
z=string+str(sm)
print(z)








