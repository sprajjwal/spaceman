from random import shuffle, choice
import os
import pyfiglet

# global variables 
alphabet = "abcdefghijklmnopqrstuvwxyz" 
word_base = [] #list of words to hold compatible with the original secret word

def load_word():
    """ loads a random word from 'words.txt'"""
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = choice(words_list)
    return secret_word

def create_word_base(secret_word, index_guessed):

    """function that creates word base that we randomize words from"""
    print("Creating word base!")
    with open('words.txt','r') as f:
        for line in f:
            for word in line.split():
                if len(word) == len(secret_word):
                    #checking each $word for different parameters to add to base
                    add_to_list = True
                    for index in index_guessed:
                        if word[int(index)] != secret_word[int(index)]:
                            add_to_list = False
                    for index in range(len(word)):
                        if index !=int(index_guessed[0]) and word[index] == secret_word[int(index_guessed[0])]:
                            add_to_list = False
                    if add_to_list:
                        word_base.append(word)
    f.close()
 
def create_index_list(secret_word, letter_guessed):
    """function that returns a string of indices for matching character
    for secret_word banana and guess 'a' it will return{1,3,5}"""
    index_list= []
    for index in range(len(secret_word)):
        if secret_word[index] == letter_guessed:
            index_list.append(index)
    return index_list

def check_new_word(secret_word, letters_guessed, new_word):
    """ checks the new word if it can replace the original secret word based on all
    the letters that have been used as guesses"""
    if len(secret_word) != len(new_word):
        return False
    for index in range(len(secret_word)):
        if secret_word[index] in letters_guessed:
            if new_word[index] != secret_word[index]:
                return False
    for letter in new_word:
        if letter in letters_guessed:
            if letter in secret_word:
                pass
            else:
                return False
    return True # False if the word passes all tests

def randomize_word(secret_word, letters_guessed):
    """function that changes the secret_word to a random word"""
    shuffle(word_base)
    for words in word_base:
        if words == secret_word:
            pass
        elif check_new_word(secret_word, letters_guessed, words):
            return words
    else: #if we don't find a replacement
        return secret_word

def is_word_guessed(secret_word, letters_guessed):
    """function that checks if the whole word is guessed"""
    for letters in secret_word:
        if letters in letters_guessed:
            pass
        else:
            return False
    return True #Game won


def get_guessed_word(secret_word, letters_guessed):
    """function that makes a string of guess for user with __e__"""
    guessed_word = ""
    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word += letters
        else: 
            guessed_word += '_'
    return guessed_word

def is_guess_in_word(guess, secret_word):
    """function that checks if guessed letter is in secret word"""
    if guess in secret_word:
        return True
    else:
        return False


def not_guessed_string(guessed_letters):
    """ helper function that returns letters that haven't been guessed yet"""
    not_guessed_string=""
    for letters in alphabet:
        if letters in guessed_letters:
            pass
        else:
            not_guessed_string += letters
    return not_guessed_string


def spaceman(secret_word):
    """ the main game function that carries out the game"""
    guesses = len(secret_word)  #number of guesses player has left
    letters_guessed = ""
    print(pyfiglet.figlet_format("Welcome to Spaceman!"))
    print("----------------------------------------")
    print("The secret word contains: " + str(len(secret_word)) + " letters")
    print("You have " + str(guesses) + " incorrect guesses, please enter one letter per round")
    print("----------------------------------------")

    while guesses > 0 : #in-game loop
        input_valid = False
        while input_valid == False: #loop for input validation
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
        os.system('clear')

        if is_guess_in_word(guess, secret_word): # correct guess
            print("Your Guess appears in the word!")
            #uncomment next line to see secret word change
            # print("Test: " + secret_word )
            if len(word_base) == 0:
                create_word_base(secret_word, create_index_list(secret_word, guess))
            secret_word = randomize_word(secret_word, letters_guessed)
            #uncomment next line to see secret word change
            # print("new secret word: " + secret_word)
        else: # incorrect guess
            print("Sorry your guess was not in the word, try again")
            guesses -= 1

        if guesses > 0: #  game running
            print("You have " + str(guesses) + " incorrect guesses left")
            print("Guessed word so far: " + get_guessed_word(secret_word, letters_guessed))
            print("These letters haven't been guessed yet: " + not_guessed_string(letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                os.system('clear')
                print(pyfiglet.figlet_format("You won!"))
                break
            else:
                print("----------------------------------------")
        else: #game lost
            print("Sorry you didn't win, try again!")
            print("The word was: " + secret_word)
            break

# Main program
def main():
    playing = True
    while playing == True: # new game loop
        playing = False
        os.system('clear')
        spaceman(load_word())
        if input("Would you like to play again?(Y/N): ") in "Yy":
            playing = True
        else:
            print("Have a good day!")

if __name__ == '__main__':
    main()
