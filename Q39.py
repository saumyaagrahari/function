def z(a):  
    x=[]
    y=[]
    i=0
    count=0
    count1=0
    while i<len(a):
        if a[i]>="a" and a[i]<="z":
            x.append(a[i])
            count+=1
        elif a[i]>="A" and a[i]<="Z":
            y.append(a[i])
            count1+=1
        i+=1
    print("small letter",x,count)
    print("capital letter",y,count1)
z("The Quick Brow Fox")