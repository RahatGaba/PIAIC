#35.Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 500, and 1000 ) against an given amount
def no_notes(a):
  Q = [10,20,50,100,500,1000]
  x = 0
  for i in range(len(Q)):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
print(no_notes(880))
print(no_notes(1000))