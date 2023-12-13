#hangman 
import time

name = input("What is your name? ")
print(f"Hello, {name}! Time to play hangman!")

time.sleep(1)
print("Start guessing...")
time.sleep(0.5)

word = "secret"
guesses = ''
turns = 10

while turns > 0:
    display_word = ''.join([char if char in guesses else '_' for char in word])
    print(display_word)

    if '_' not in display_word:
        print("You won!")
        break

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong. You have", turns, "more guesses.")

    if turns == 0:
        print("You lose!")
