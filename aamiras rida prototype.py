print("Thank You For Visiting Aamiras Rida")
name = input("What Is Your Name Young Lady?\n")
if name == "jamila" or name == "tahera" or name == "fatema":
    evil_status = input("Will you pay the money for your rida within 20 days? - ")
    payment = int(input("How many people do you owe money to? - "))
    if evil_status == "no" and payment >= 3:
     print("You're not welcome here, " + name + " get out of here!!!!!")
     exit()
    else:
        print("Oh, so you are one of those good " + name + "s. Come on in")
else:
    print("Hello " + name + ", Welcome To Aamiras Rida, Where You Get The Best Quality Ridas For All Occasions.\n")

menu = "1) Shaadi Wear", "2) Party Wear", "3) Casual", "4) Semi-Casual", "5) Pattern", "6) Hand-Work", "7) Embroidery"
print(name + " ,what kind of ridas are you looking for? , here are some options:\n")
print(menu)
order = input("Which kind of rida do you like - ")

if order == "Shaadi Wear":
    price = 10000
elif order == "Party Wear":
    price = 4500
elif order == "Casual":
    price = 2200
elif order == "Semi-Casual":
    price = 2700
elif order == "Pattern":
    price = 2600
elif order == "Hand-Work":
    price = 4000
elif order == "Embroidery":
    price = 3500
else:
    print("Sorry, We don't have what you're looking for.")
quantity = int(input("how many ridas will you like to have: \n"))
total = price * quantity
tax = total/100 * 18

print("Sounds Good " + name + ",we'll have that " + order + " Rida, ready for you in a couple of days\n")
print("The Total amount You Have To Pay Is: " + str(total) + "/- Rs\n" + "The amount with gst: " + str(tax+total) + "/- Rs")

