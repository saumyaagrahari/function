# Ek function define kijiye jo ki drivers ki speed check karega. Aur ye function speed naam ka ek
# parameter lega.
# Agar speed 70 se kam hai to ye “ok” print karega.
# Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 1 point dega (ye 70 ko count
# nahi karega).
# example ke liye agar speed 80 hai to print karega “points:2” .
# Agar driver ko 12 points se jyaada points milte hai to , function “License suspended” print karega.

# input
# 85
# 135
# Output
# 3
# “License suspended”



# def speed(a):
#     if a<70:
#         print("ok")
#     elif a>70 and a<135:
#         print("points:",+2)
#     else:
#         print("License suspended")
# speed (int(input("enter the number")))