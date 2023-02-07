
# defines correct word as a string and as a list
correct_word = "hangman"
correct_word_list = []
for char in correct_word:
    correct_word_list.append(char)

# defines previously guessed chars list and correctly guessed chars list, initially empty
guessed_chars = [] 
correct_guessed_chars = []
for i in range(len(correct_word_list)):
    correct_guessed_chars.append("_")

# defines function that allows user to input a character as a guess
def guess_letter():
    guess = input("Guess a letter: ")
    if guess in guessed_chars:
        return "You already guessed that letter! "
    guessed_chars.append(guess)
    return guess

def main():

    lives = 6

    while lives > 0:
        guess = guess_letter()

        # pass if letter was already guessed
        if guess == "You already guessed that letter! ":
            print(f"You have {lives} guesses left." )
            pass

        # if guess is correct, add it to list at the right index
        if guess in correct_word_list:
            print("============\nCorrect! ")
            
            for i in range(len(correct_word_list)):
                if correct_word_list[i] == guess:
                    correct_guessed_chars[i] = guess

            print(" ".join(map(str, correct_guessed_chars)))

            # if there are no more underscores in list, that means all letters have been guessed
            if "_" not in correct_guessed_chars:
                print("You win! ")
                break
        
        # if guess is incorrect, subtract a life
        else:
            lives = lives - 1
            print(f"=================\nIncorrect. \nYou have {lives} guesses left.")
            print(" ".join(map(str, correct_guessed_chars)))

    # if lives is 0, you lose
    if lives == 0:
        print("You lose!")

main()
