#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
number=int(input("Enter any number: "))
if number%2==0:
    print(str(number)+ " is even")
else:
    print(str(number)+ " is odd")