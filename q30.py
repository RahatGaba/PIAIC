#Write a Python program to count the number occurrence of a specific character in a string 
string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("The total Number of Times ", char, " has Occurred = " , count)