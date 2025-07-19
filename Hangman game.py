import random

# List of predefined words
word_list = ["yashu", "amma", "appa", "chintu", "suppi"]

# Randomly choose a word from the list
word = random.choice(word_list)

# Create a list to hold guessed letters (start with underscores)
guessed_word = ["_"] * len(word)

# Set the number of allowed incorrect guesses
max_attempts = 6
wrong_guesses = 0

# List to store all guessed letters
guessed_letters = []

print("🎯 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Main game loop
while wrong_guesses < max_attempts and "_" in guessed_word:
    print("\nCurrent word: ", " ".join(guessed_word))
    print(f"Wrong guesses left: {max_attempts - wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    # Check for invalid input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
