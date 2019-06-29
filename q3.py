#Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user
def multiple(m, n):
	return True if m % n == 0 else False
print(multiple(20, 5))
print(multiple(7, 2))