n = int(input("Enter the number of fibonacci elements:"))
t1, t2 = 1, 1
print(t1),
print(t2),
t3=0
while(t3<n):
	t3 = t1 + t2
	if(t3<=n):
		print(t3)
	t1 = t2
	t2 = t3
