#16.Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
x1=int(input("Enter the value of x1: "))
x2=int(input("Enter the value of x2: "))
y1=int(input("Enter the value of y1: "))
y2=int(input("Enter the value of y2: "))
ans=((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))
sqrt = ans ** 0.5
print("Distance between these two points is : "+str(sqrt))