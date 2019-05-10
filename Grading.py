name=input("Enter your name ")
pro=int(input("Enter marks of Programming Fundamentals out of 100: "))
isl=int(input("Enter marks of Islamiat out of 100: "))
cs=int(input("Enter marks of Communication Skills out of 100: "))
cal=int(input("Enter marks of Calculus out of 100: "))
itc=int(input("Enter marks of Introduction to Computer out of 100: "))
Ave=(pro+isl+cs+cal+itc)/5
print("\t\t\tMARKSHEET OF 1ST SEMESTER")
print("\n\t\t\tName",name)
print("\n\t\t\tMarks of Subjects")
print("\nProgramming Fundamental   ",pro,"/100")
print("Islamiat                  ",isl,"/100")
print("Introduction to Computer  ",itc,"/100")
print("Communication Skills      ",cs,"/100")
print("Calculus                  ",cs,"/100")
print("\nAverage of marks",Ave)
if Ave>=80:
    print("A+ Grade")
elif Ave>=70:
    print("A Grade")
elif Ave>=60:
    print("B Grade")
elif Ave>=50:
    print("C Grade")
elif Ave>=40:
    print("D Grade")
else:
    print("You are fail")
