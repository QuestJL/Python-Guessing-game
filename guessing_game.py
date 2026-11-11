import random 
attempts = 0

secret_number = random.randint(1, 10)

guess = int(input("Guess any number:")) 
attempts += 1 
while guess != secret_number: 

    if guess > secret_number: 
        print("Too high. Try again!")
    elif guess < secret_number: 
        print("Too low. Try again") 

    guess = int(input("Guess again")) 
    attempts += 1 

print("Correct guess")
print(f"You got it in {attempts} attemps!") 