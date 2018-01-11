import random
comp = random.randint(1,4)
user = int(input("Enter your choice:\n\trock(1)\n\tpaper(2)\n\tscossor(3)\n"))

if(comp==1):
	print("computer is Rock")
elif(comp==2):
	print("computer is Paper")
else:
	print("computer is Scissor")

if(user==1):
	print("You chose Rock")
elif(user==2):
	print("You chose Paper")
else:
	print("You chose Scossor")


if(comp==user):
	print("Its a draw!")
elif((user==1 and comp==3) or (user==2 and comp==1) or (user==3 and comp==2)):
	print("You Win!")
else:
	print("computer Wins!")
