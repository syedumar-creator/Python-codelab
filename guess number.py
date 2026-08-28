import random
target=random.randint(1,100)
while True:
    user=input("Guess the number (1-100) or q to Quit: ")
    if(user=="q"):
        break
    user=int(user)
    if(user==target):
        print("Congratulations, Your Guess is correct.")
    elif(user<target):
        print("Your Guess was too small, Try Again...")
    else:
        print("Your Guess was too large, Try Again...")
print("------GAME OVER------")