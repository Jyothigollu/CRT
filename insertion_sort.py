a=[14,10,5,4,15,25,12]
for i in range(1,len(a)):
    min=i-1
    n=a[i]
    while a[min]>n and min>=0:
        a[min+1],a[min]=a[min],a[min+1]
        min=min-1
print(a)
        