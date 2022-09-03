print("ENTER THE OPERATION YOU WANT:")
print("1 . ADD\n" + "2 . SUBTRACT\n" + "3 . MULTIPLY\n" + "4 . DIVIDE\n" + "5 . REMAINDER OF THE TWO NUMBERS DIVIDED\n" + "6 . NUMBER RAISE TO THE POWER OF\n" + "7 . Factorial of the number \n")
operation = input("WHAT OPERATION WOULD YOU LIKE TO PERFORM : ")
if operation == "1":
    num1 = float(input("What is your first number : "))
    num2 = float(input("What is your second number : "))
    sum = num1 + num2
    print("The sum of the two numbers you entered is - " + str(sum))
elif operation == "2":
    num1 = float(input("What is your first number : "))
    num2 = float(input("What is your second number : "))
    sum = num1 - num2
    print("The difference of the two numbers you entered is - " + str(sum))
elif operation == "3":
    num1 = float(input("What is your first number : "))
    num2 = float(input("What is your second number : "))
    sum = num1*num2
    print("The multiplication of the numbers you entered is - " + str(sum))
elif operation == "4":
    num1 = float(input("What is your first number : "))
    num2 = float(input("What is your second number : "))
    sum = num1/num2
    print("The division of the numbers you entered is - " + str(sum))
elif operation == "5":
    num1 = float(input("What is your first number : "))
    num2 = float(input("What is your second number : "))
    sum = num1%num2
    print("The remainder of the numbers you entered is - " + str(sum))
elif operation == "6":
    num1 = float(input("What is your first number : "))
    num2 = float(input("What is your second number : "))
    sum = num1**num2
    print(str(num1) + " raise to " + str(num2) + " is equal to - " + str(sum))

if __name__ == '__main__' and operation == "7":
    number = int(input("PLEASE ENTER THE NUMBER OF WHICH YOU WANT THE FACTORIAL OF :\n"))
    factorial = 1
    if (number<0):
        print("Error : Factorial of a negative number is not defined.")

    elif (number==0):
        print(1)

    else:
          for i in range(1, number+1):
              factorial = factorial*i
          print("The factorial of", number, "is", factorial)

else:
    print("Your Operation Is Invalid. Please Try Again!!!!!")