from hangman_art import logo, stages
from hangman_words import word_list
import random

print(logo)

lives = 6

# Choose a random word form the word list
chosen_word = random.choice(word_list)

# Show the user empty dashes equal to word length
place_holder = "_" * len(chosen_word)
print(f"Word to guess: {place_holder}")

game = True
#check if guessed letter is in the word or not and take the action accordingly
display = ["_"] * len(chosen_word)

while game:
    # Ask the user to guess a letter of this word
    guess = input("Make a Guess: ").lower()

    # Check if entering the same guess again
    if guess in display:
        print(f"You have already guessed {guess}")

    
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            print("wow! that's right 👍")
            display[i] = guess
        else:
            pass

    print("".join(display))

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life. 🙁")
        lives -= 1

        if lives == 0:
            game = False
            print(f"****************** IT WAS {chosen_word}. YOU LOSS 🙄 *********************")
    
    if "_" not in display:
        game = False
        print("*************** YOU WIN 😃 *****************")
    
    # show hangman stages 
    print(stages[lives])