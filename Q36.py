def a(list1):
    list2=[]
    i=0
    while i<len(list1):
        if  list1[i] in list2:
            pass
        else:
            list2.append(list1[i])
        i=i+1
    print(list2)
a([1,2,3,3,3,3,4,5])