def number(a):
    # a=[10,[1,2,3],[4,5],[6],[7,8,9],[10]]
    i=0
    sum=0
    while i<len(a):
        if(str(a[i]).isdigit()):
            sum=sum+a[i]
        else:   
            j=0
            while j<len(a[i]):
                sum=sum+a[i][j]
                j=j+1
        i=i+1
    print(sum)
number([10,[1,2,3],[4,5],[6],[7,8,9],[10]])


