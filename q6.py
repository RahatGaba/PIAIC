#Write a Python program to get the volume of a sphere, please take the radius as input from user. V=4 / 3 πr3
radius=float(input("Enter radius in inch to calculate the volume of sphere: "))
volume=4/3*(3.141*radius*radius*radius)
print("Volume of sphere =" +str(volume)+" in³")
