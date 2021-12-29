# .Write function bmi that calculates body mass index (bmi = weight / height2).
def a(bmi): 
    if bmi <= 18.5:
        print("Underweight")
    if bmi <= 25.0:
        print("Normal")
    if bmi <= 30.0:
        print("Overweight")
    if bmi > 30:
        print("Obese")
a(bmi=float(input("enter the number:")))            
        