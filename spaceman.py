import random
alphabet = "abcdefghijklmnopqrstuvwxyz"

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letters in secret_word:
        if letters in letters_guessed:
            pass
        else:
            return False
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessed_word = ""
    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word += letters
        else: 
            guessed_word += '_'
    return guessed_word
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
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
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    guesses = 7  #number of guesses player has left
    letters_guessed = ""

    #TODO: show the player information about the game according to the project spec
    print("----------Welcome to Spaceman!----------\n\n\n")
    print("The secret word contains: " + str(len(secret_word)) + " letters")
    print("You have " + str(guesses) + " incorrect guesses, please enter one letter per round")
    print("----------------------------------------")

    while is_word_guessed(secret_word, letters_guessed) == False:
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        input_valid = False
        while input_valid == False:
            guess = input("Enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                input_valid = True
            elif len(guess) != 1:
                print("Please only enter one letter at a time")
            elif guess.isalpha() == False:
                print("Please only enter a letter")
            elif guess in letters_guessed:
                print("You have alreadye guessed " + guess)

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
            print("----------------------------------------")
        else:
            print("Sorry your guess was not in the word, try again")
            print("Sorry you didn't win, try again!")
            print("The word was: " + secret_word)
            break
        #TODO: check if the game has been won or lost





#These function calls that will start the game
spaceman(load_word())