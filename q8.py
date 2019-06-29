# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged 
def new_string(str):
  if len(str) >= 2 and str[:2] == "is":
    return str
  return "is" + str

print(new_string("rahat"))
print(new_string("is rahat"))
