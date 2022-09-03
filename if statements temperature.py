temperature= float(input("what is the temperature? "))
if temperature>30:
    print("It's a hot day")
    print("Drink Plenty Of Water")
elif temperature>20: #(20,30]
    print("IT's a nice day")
    print("go out for a walk")
elif temperature>10: #(10,20]
    print("It's a bit cold")
    print("wear a jacket if you are not canadian")
else:
    print("It's cold")
    print("stay at home and on a heater")
