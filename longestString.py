strings = input("Enter the strings seperated by a space: ").split()
maxi=0
for string in strings:
	if(len(string)>maxi):
		maxi = len(string)
		best = string

print("Maximum length of given strings is", maxi, " and the string is", best)
