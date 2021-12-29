# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameterko hume check 
# karana hai ki vo perfect number hain ya nahi. Iske baad uss function ko use karke ek program likhiye 
# jo ki 1 se1000 tak sabhi perfect numbers ko print kare.[ hum ek aise integer number ko perfect 
# number kahenge jo ki uske sabhi factors ( including 1 & excluding itself) ka sum uss number 
# ke barabar hota hai.


# "6 ek perfect number hai" 
# 6=1+2+3
# 6,28,496


# The program output is also shown below. n = int(input("Enter any number: ")) sum1 = 0 for i in range
# (1, n): if(n % i == 0): sum1 = sum1 + i if (sum1 == n): print("The number is a Perfectnumber! ") 
# else: print("The number is not a Perfect number!

n=int(input("enter the number:"))
def a(n):
    sum1=0
    for i in range (1,n):
        if (n % i == 0):
            sum1 = sum1 +i
            if (sum1 == n):
                print("The number is a Perfectnumber!")
                break
        else:
            print("The number is not a Perfect number!")
            break
a(n)
