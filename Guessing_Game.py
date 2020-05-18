import random

nw = 0    # Initialisied the number of wrong attempts
comGuess = random.randint(0, 100)  # comGuess is initialised with a random number between 0 and 100

while True:  # loop will run until encountered with the break statement(user enters the right answer)
    userGuess = int(input("Enter your guessed no. b/w 0-100:"))  # user input for guessing the number
    if userGuess < comGuess:  # if number guessed by user is lesser than the random number than the user is told to guess higher and the random number comGuess is changed to a new random number between a and 100
        print("Your guess is low.")

        nw += 1

    elif userGuess > comGuess:  # if number guessed by user is greater than the random number than the user is told to guess lower and the random number comGuess is changed to a new random number between 0 and a
        print("Your guess is high.")
 
        nw += 1

    else:  # if guessed correctly the loop will break and the player will win
        print(f"Guessed Corectly in {nw} attempts!")
        break
