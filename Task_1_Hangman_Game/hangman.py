
import random

# List of words
words = ["python", "computer", "program", "developer", "keyboard"]

# Function to display the word
def display_word(word, guessed_letters):
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    print("Word:", result)


# Main game function
def play_hangman():
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman Game!")
    print("Guess the secret word.")

    while attempts > 0:
        display_word(word, guessed_letters)

        print("Attempts left:", attempts)
        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

        # Check winning condition
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You won!")
            print("The word was:", word)
            return

    print("Game Over!")
    print("The correct word was:", word)


# Start the game
if __name__ == "__main__":
    play_hangman()
