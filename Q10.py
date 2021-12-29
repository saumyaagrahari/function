# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain"
# agar dono numbers even (2 se divide hote hain) nahi toh print kare "Dono numberseven nahi hai"

# def check_numbers(a,b):
#     i=0
#     sum=0
#     while i<(len(a)):
#         # j=0
#         # while j<(len(a)):
#             sum=a[i]+b[i]
#             # sum=sum+1
#             if sum%2==0:
#                 print("Dono even hain")
#             else:
#                 print("Dono numbers even nahi hai")
#         # j=j+1
#     i=i+1
# check_numbers([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])

# a=[34,45,6,7,8,9]
# b=[4,5,7,8,2,2]
def check(a,b):
    i=0
    while i<(len(a)):
        sum=a[i]+b[i]
        if sum%2==0:
            print("even")
        else:
            print("not even")
        i+=1
check([34,45,6,7,8,9],[4,5,7,8,2,2])