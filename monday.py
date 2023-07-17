marks=int(input("Enter your marks?"))
if marks>80 and marks <=100:
	print("Congrats!You have scored grade A")
elif marks>60 and marks <=80:
	print("You have scored grade B")
elif marks>50 and marks <=60:
	print("You have scored grade C")
elif marks>40 and marks <=50:
	print("You have scored grade D")
else:
	print("You have failed!")
