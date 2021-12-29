# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length jyaada 
# hogi use print karega aur agar dono strings ki length equal hui to dono ko line by line print karega.
#  Hint :- use len() builtin function..

# input
# function_name(“hello”,”welcome”)
# function_name(“sonu”,”monu”)
# Output
# welcome
# sonu
# monu

a=input("enter anything:")
b=input("enter something:")
def function_name(a,b):
        if len(a)>len(b):
            print(a)
        elif len(a)<len(b):
            print(b)
        else:
            (a,b)
function_name(a,b)
