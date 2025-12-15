import random
words = ["python", "java", "apple", "banana", "computer"]
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("Word:", display_word)

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue
    guessed_letters.append(guess)

    if guess not in secret_word:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print(f"Remaining attempts: {max_wrong - wrong_guesses}\n")
    else:
        print("✅ Correct guess!\n")

if wrong_guesses == max_wrong:
    print("💀 Game Over!")
    print("The word was:", secret_word)
