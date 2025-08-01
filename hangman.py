import random
# List of predefined words
word_list = ["apple", "tiger", "house", "robot", "chair"]

# Randomly select a word
word = random.choice(word_list)
guessed_word = ["_"] * len(word)
guessed_letters = []
max_guesses = 6
wrong_guesses = 0

print("Welcome to Hangman!")

while wrong_guesses < max_guesses and "_" in guessed_word:
    print("\nWord: ", " ".join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess.")
        wrong_guesses += 1
        print(f"Incorrect guesses left: {max_guesses - wrong_guesses}")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nYou lost. The word was:", word)