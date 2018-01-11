def isPalindrome(s):
	for i in range(0, int(len(s)/2)):
		if(s[i] != s[len(s)-i-1]):
			return False
	return True


string = input("Enter a string to check whether it is a palindrome or not: ")

if(isPalindrome(string)):
	print("Yes, it is a palindrome")
else:
	print("No, it is not a palindrome")
