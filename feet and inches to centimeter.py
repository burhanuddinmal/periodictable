print("WHAT IS YOUR HEIGHT")
h_feet = float(input("Your Height In Feet: "))
h_inches = float(input("Your Height In Inches: "))
h_inches += h_feet*12
h_cm = round(h_inches*2.54,1)
print("Your Height In Centimeters: " + str(h_cm))