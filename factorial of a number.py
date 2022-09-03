if __name__ == '__main__':
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