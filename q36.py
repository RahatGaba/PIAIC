#Write a program to check whether given input is palindrome or not
my_str =input("Enter a string: ")
my_str = my_str.lower()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")