#Write a Python program to create the multiplication table (from 1 to 10) of a number 
number=int(input("Enter num to print multiplication table :"))
for i in range(1,11):
    c=number*i
    print(str(number)+"x"+str(i)+"="+str(c))
