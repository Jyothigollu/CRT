a=[4,1,4,2,5,1,5,3,10,20,15]
b=[5,1,4,3,15,30]
r=list()
j=0
d={}
for i in range(len(b)):
    d[b[i]]=a.count(b[i])
print(d)
l=list((set(a).difference(set(b))))
print(l)
for i,j in d.items():
    r.append((str(i)+' ')*j)
print(r)
print(r+l)

