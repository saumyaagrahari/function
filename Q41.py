# def a(i):
#     while i<=10:
#         print(i)
#         i=i+2
# a(2)

# def b(i):
#     while i<10:
#         print(i)
#         i=i+3
# b(3)


# def a(i):
#     while i<=100:
#         if i%2==0:
#             print("even number",i)
#         else:
#             print("odd number",i)
#         i=i+1
# a(1)


def x(num):
    count=0
    i=1
    while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("prime number:",num)
    else:
        print("not prime number:",num)
x(float(input("enter the number:")))



# i=0
# while i<=5:
#     j=0
#     while j<=i:
#         print(i)
#         j=j+1
#         print()
#     i=i+1