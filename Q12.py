# eligible_for_vote name ka function likho jo ki user ko bataye ki vo (he/she) vote 
# de sakta hai ya nahi. ( Consider minimum age of voting to be 18. )

def eligible_for_vote ():
    a=int(input("enter the number:"))
    if a<18:
        print("“not eligible “")
    else:
        print("“you are eligible”")
eligible_for_vote()
