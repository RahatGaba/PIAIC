#Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)
n=int(input("Enter the value of n : "))
ans=n+n*n+n*n*n
print("The value of n+nn+nnn = "+str(ans))