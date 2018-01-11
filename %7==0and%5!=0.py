print("Numbers from 2000 to 3200 which are divisible by 7 but not 5 are given below:\n")
for i in range(2000, 3201):
	if i%7==0 and i%5!=0:
		print(i, ", ", end="")
