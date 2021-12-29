# def a(list):
#     count=0
#     for i in list:
#         if len(i)>2:
#             if i[0]==i[-1]:
#                 count+=1
#     print(count)
# a(["aba","abc","1221","xyz"])


def a(list):
    i=0
    count=0
    while i<len(list):
        if len(list[i])>2:
            if list[i][0]==list[i][-1]:
                count+=1
        i+=1
    print(count)
a(["aba","abc","1221","xyz"])
      
