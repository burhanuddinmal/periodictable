height= float(input("Enter Your Length: "))
unit = input("(I)nch or (C)enti: ")
if unit.upper() == "I":
   converted = 2.54*height
print("Your Height In Centimeters: " + str(converted))
