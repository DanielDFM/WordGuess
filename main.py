
import random

# File with the word list
LEXICON_FILE = "Lexicon.txt"

# Number of guesses player starts with
INITIAL_GUESSES = 5

# Initial hints
INITIAL_HINTS = 3

# Spaces to clean code
SPACES = "                                                          "

# Spaces for intro message
INTRO_SPACES = "                                              "

def main():
    """
    Select the secret word from the file and run using that secret word
    """
    turn = 'Y'
    while True:
        if turn == 'Y':
            secret_word = get_word()
            play_game(secret_word)
            turn = input(SPACES+"Do you want to play again? (Y/N): ")
            turn = turn.upper()
        elif turn == 'N':
            break
        else:
            print("")
            print(SPACES+"Please Enter Y or N")
            turn = input(SPACES+"Do you want to play again? (Y/N): ")
            turn = turn.upper()
    print("")
    print(SPACES+"Thanks for playing !")




def play_game(secret_word):

    print(INTRO_SPACES+"                  WELCOME TO THE WORD GUESS GAME BY DANIEL MONTEIRO                   ")
    print(INTRO_SPACES+"                       You can only make 5 mistakes                         ")
    print(INTRO_SPACES+"                        Press '!' for a hint                          ")
    print(INTRO_SPACES+"                              Good luck and have fun                                  ")

    word = secret_word             # When a letter is guesses correctly and that letter is deleted from words
    guesses = INITIAL_GUESSES       # Maximum wrong guesses allowed
    blank = ""                    # adds a blank space
    length = len(secret_word)     # Length of the secret word
    won = False                   # Check if user won or lost
    hint_count = INITIAL_HINTS    # Maximum hints allowed

    for i in range(length):       # prints the initial blank word
        blank = blank + "-"

    while guesses != 0:
        ind = 0
        print(SPACES+"Your word looks like: " + blank)
        guessed = input(SPACES +"Please enter your guess. You have " + str(guesses) + " Guesses and " + str(hint_count) + " Hints left: ")
        guessed = guessed.upper()

        if len(guessed) == 1:
            for letter in secret_word:
                if guessed == letter:
                    if guessed in word:
                        ind = word.index(guessed)
                        blank = blank[:ind] + guessed + blank[ind+1:]
                        word = word[:ind] + "-" + word[ind + 1:]
                    else:
                        print(SPACES+"You already chose " + guessed)

            # code for hints
            if guessed == '!':
                if hint_count != 0:
                    hint_word = ""
                    for lt in word:
                        if lt != '-':
                            hint_word = hint_word + lt
                    hint_len = len(hint_word)
                    ind = random.randint(0, hint_len - 1)
                    hint = hint_word[ind]
                    print(SPACES+"Hint: " + hint)
                    print("")
                    guesses -= 1
                    hint_count -= 1
                else:
                    print(SPACES+"Sorry, No Hints left")
                    print("")

            # Checks if guessed letter is correct or not
            if guessed not in secret_word:
                if guessed != '!':
                    print(SPACES+"There are no " + guessed + "\'s in the secret word")
                    print("")
                    guesses -= 1
            else:
                if guessed != '+':
                    print(SPACES+"That Guess was correct")
                    print("")


            if blank == secret_word:
                won = True
                break
            else:
                won = False

        else:
            print(SPACES+"Type a single letter here, ")
            print("")

    # Prints winner or loser message
    if won:
        print(SPACES+"Congratulations! You WON. ")
        print(SPACES +"You took " + str(8 - guesses) + " Guesses and " + str(5 - hint_count) + " Hints to guess the word: " + secret_word)
        print("")
    else:
        print(SPACES+"Sorry, you lost. The secret word was: " + secret_word)
        print("")



def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.
    """
    word = []
    with open(LEXICON_FILE) as f:
        for words in f:
            words = words.strip()
            word.append(words)
    length = len(word) - 1
    rand = random.randint(0, length-1)
    return word[rand]





if __name__ == "__main__":
    main()