s=input()
s1=set(s)
d={}
for i in s1:
    k=s.count(i)
    d[i]=k
print(d)
d=sorted(d.items(),key=lambda x:(x[1],x[0]))
print(list(d))
