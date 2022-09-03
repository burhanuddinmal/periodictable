print("WHAT IS THE LENGTH?")
height = float(input("Height: "))
unit = input("(M)t or (F)t or (I)ch or (N)for meters to inches : ")
if unit.upper() == "M" :
    converted = height*3.28084
    print("Your Length In Feet: " + str(converted))
elif unit.upper() == "I":
    converted = height/39.3701
    print("YOUR LENGTH IN METERS: " + str(converted))
elif unit.upper() == "N":
    converted = height*39.3701
    print("Your Length In Inches: " + str(converted))
else:
    converted = height/3.28084
    print("Your Height In Meters: " + str(converted))