import random
number = random.randint(1,100)
print("You have 10 chance to guess the number correctly.The number is between 1 to 100")
for i in range(10):
	guess_no = int(input("Guess the number :"))
	if guess_no == number :
		print(f"YOU WIN!!!\nYou guessed it in {i+1} times.")
		break
	else:
		if i == 9:
			print("YOU LOSE")
		else:
			if guess_no > number:
				print("HINT:number is smaller than you entered.")
			else:
				print("HINT:number is larger than you entered.")
