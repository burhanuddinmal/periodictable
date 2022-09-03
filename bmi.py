print("ENTER YOUR HEIGHT AND WEIGHT: ")
height = float(input("enter your height: "))
weight = float(input("enter your weight: "))
if height>180 and weight <= 72:
    print("you are underweight: ")
elif height>160 and weight <= 55:
    print("you are underweight: ")
elif height>140 and weight <= 45:
    print("you are underweight: ")
else:
    print("Your weight is normal.")