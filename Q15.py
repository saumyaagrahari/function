# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter lega aur 0 se 
# limit tak ke beech ke sabhi even aur odd numbers ko label ke saath print karega jaisa ki niche
#  dikhaya gaya hai.


# input
# 3
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


def showNumbers(a):
    # a=int(input("enter the number:"))
    if a % 2==0:
        print(a,"EVEN")
    else:
        print(a,"ODD")
showNumbers(3)

