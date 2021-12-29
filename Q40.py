# def x(a,b):
#     # a="4","5"
#     # b="34","5"
#     a=str(4+5)
#     b=str(34+5)
#     print(type(a))
#     print(type(b))
#     print(a,b)
# x ("4","5")
#   ("34","5")

# print("Enter the Name of File: ", end="")
# filename = input()
# try:
#     fo = open(filename, "r")
#     print("\n----The content of file \"", filename, "\"----", sep="")
#     print(fo.read())
# except FileNotFoundError:
#     print("\nThe file \"", filename, "\" doesn't found.", sep="")

# # fo = open("codescracker.txt", "r")
# # print(fo.read(10))

print("Enter the Name of File: ", end="")
filename = input()
try:
    fo = open(filename, "r")
    print("\n1. Read Whole Content.")
    print("2. Read Only Specified Number of Bytes.")
    print("Enter Your Choice (1 or 2): ", end="")
    try:
        choice = int(input())
        if choice==1:
            print("\n----The content of file \"", filename, "\"----", sep="")
            print(fo.read())
        elif choice==2:
            print("\nEnter the Number of Bytes to Read: ", end="")
            try:
                nob = int(input())
                print("\n----The First ", nob, " characters of file \"", filename, "\"----", sep="")
                print(fo.read(nob))
            except ValueError:
                print("\nInvalid Input!")
    except ValueError:
        print("\nInvalid Input!")
except FileNotFoundError:
    print("\nThe file \"", filename, "\" doesn't found.", sep="")