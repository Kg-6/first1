dt=[{'name':2},{'name':9},{'name':3}]
'''k=list(sorted(dt.keys()))
k.sort()
d={(i,dt[i]) for i in k}
print(k)'''
print( sorted(dt,key=lambda item:item['name']))
