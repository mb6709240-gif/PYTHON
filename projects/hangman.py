hangman (word guess game)

import random

words = ["python", "java", "apple", "train", "house"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong!")

    if "_" not in guessed:
        print("\n🎉 You guessed the word:", word)
        break

if "_" in guessed:
    print("\n💀 You lost! The word was:", word)


