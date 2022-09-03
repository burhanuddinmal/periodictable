weight = float(input("weight: "))
unit = input("(K)g or (L)bs or (G)ms: ")
if unit.upper() == "K":
    converted=weight/0.45
    print("weight in Lbs: "+ str(converted))
elif unit.upper() == "G":
    converted= weight/1000
    print("weight in Kgs:" + str(converted))
else:
    converted=weight*0.45
    print("weight in Kgs: "+ str(converted))
