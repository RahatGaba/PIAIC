#Write a Python program to get the Fibonacci series between 0 to 50
nterms = 50
n1 = 0
n2 = 1
count = 0
print("Fibonacci sequence upto",nterms,":")
while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1