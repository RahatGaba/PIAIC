#.Write a Python program to calculate body mass index. 
height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))
