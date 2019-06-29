#.Input a text and count the occurrences of vowels and consonant
def vowel_count(str): 
	count = 0
	vowel = set("aeiouAEIOU") 
	for alphabet in str: 
		if alphabet in vowel: 
			count = count + 1
	print("No. of vowels :", count) 
def con_count(str2): 
	count1 = 0
	con = set("bBCcDdfFGgHhjJKkLlMmNnpPQqRrsSTtvVWwxXYyzZ")  
	for alphabets in str2: 
		if alphabets in con: 
			count1 = count1 + 1
	print("No. of Contstants :", count1) 
str = input("Enter string to check: ")
vowel_count(str) 
con_count(str)
