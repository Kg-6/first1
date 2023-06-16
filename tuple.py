t=[(1,7),(0,5),(2,1)]
print(t[0])
t1=sorted(t,key=lambda x:x[0])
print(t1)
l=int(input("enter the no of elements in list:"))
l2=[]
for i in range(l):
    t1,t2=input().split(',')
    l2.append([int(t1),int(t2)])
print(l2)
l3=sorted(l2,key=lambda x:x[1])
print(l3)