import random

words = ["python", "apple", "chair", "mouse", "water"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print(" ".join(guessed))
    guess = input("Enter a letter: ")

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed:
    print("You won! Word is:", word)
else:
    print("You lost! Word was:", word)