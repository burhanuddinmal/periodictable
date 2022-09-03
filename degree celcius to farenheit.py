print("What is the temperature? ")
temp = float(input("temperature: "))
unit = input("(C)el or (F)et: ")
if unit.upper() == "C":
    converted = 1.8*temp + 32
    print("Temperature In Fahrenheit: " + str(converted))
else:
    converted = (temp-32)/1.8
    print("Temperature In Degree Celcius: " + str(converted))
