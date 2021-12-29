# Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke beech ke number
#  jo ki 3 aur 5 ke multiples hain unka sum print karega.jaisa ki niche dikhaya gya hai.

# input
# 10
# 3 aur 5 ke multiples => 3, 5, 6, 9, 10
# output-33


def limit(a,b,c,d,e):
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# d=int(input("enter the number:"))
# e=int(input("enter the number:"))
    if a % 3==0  or  a % 5==0:
        if b % 3==0  or  b % 5==0:
            if c% 3==0  or  c % 5==0:
                if d% 3==0  or  d % 5==0:
                    if e% 3==0  or  e % 5==0:
                        print(a+b+c+d+e)
limit(3,5,6,9,10)

