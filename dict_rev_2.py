d={1:'a',2:'b',3:'c'}
l=[]
m=[]
for i,j in d.items():
    l.append(i)
    m.append(j)
for i in range(0,len(l)):
    d.pop(l[i])
    d[m[i]]=l[i]
print(d)
