import random
alphabet = "abcdefghijklmnopqrstuvwxyz"

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letters in secret_word:
        if letters in letters_guessed:
            pass
        else:
            return False
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word += letters
        else: 
            guessed_word += '_'
    return guessed_word
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet



def is_guess_in_word(guess, secret_word):
   #check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False


#helper function that returns letters that haven't been guessed yet
def not_guessed_string(guessed_letters):
    not_guessed_string=""
    for letters in alphabet:
        if letters in guessed_letters:
            pass
        else:
            not_guessed_string += letters
    return not_guessed_string

def spaceman(secret_word):
  
    guesses = 7  #number of guesses player has left
    letters_guessed = ""

    #TODO: show the player information about the game according to the project spec
    print("----------Welcome to Spaceman!----------\n\n\n")
    print("The secret word contains: " + str(len(secret_word)) + " letters")
    print("You have " + str(guesses) + " incorrect guesses, please enter one letter per round")
    print("----------------------------------------")

    while guesses > 0 :
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        input_valid = False
        while input_valid == False:
            guess = input("Enter a letter: ").lower()
            if guess in letters_guessed:
                print("You have alreadye guessed " + guess)
            elif len(guess) == 1 and guess.isalpha():
                input_valid = True
            elif len(guess) != 1:
                print("Please only enter one letter at a time")
            elif guess.isalpha() == False:
                print("Please only enter a letter")

        letters_guessed += guess
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("Your Guess appears in the word!")
        else:
            print("Sorry your guess was not in the word, try again")
            guesses -= 1
        #TODO: show the guessed word so far
        if guesses > 0:
            print("You have " + str(guesses) + " incorrect guesses left")
            print("Guessed word so far: " + get_guessed_word(secret_word, letters_guessed))
            print("These letters haven't been guessed yet: " + not_guessed_string(letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                print("You won!")
                break
            else:
                print("----------------------------------------")
        else:
            print("Sorry you didn't win, try again!")
            print("The word was: " + secret_word)
            break

#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())