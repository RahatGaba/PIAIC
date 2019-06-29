#18.Write a Python program to calculate the hypotenuse of a right angled triangle 
print("The right angled triangle consist of three sides, hypotenuse(h), opposite(o), and adjacent(a)")
adjacent=int(input("Enter the value of adjacent side: "))
opposite=int(input("Enter the value of opposite side: "))
ans=(adjacent**2+opposite**2)
final_ans=ans**0.5
print("Hypotenuse of a right angled triangle is : "+str(final_ans))
