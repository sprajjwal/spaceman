import random
import os
alphabet = "abcdefghijklmnopqrstuvwxyz"
word_base = []

#function to load a random word from the file
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

#function that creates word base that we randomize words from
def create_word_base(secret_word, index_guessed):
    print("Creating word base!")
    with open('words.txt','r') as f:
        for line in f:
            for word in line.split():
                if len(word) == len(secret_word):
                    add_to_list = True
                    for index in index_guessed:
                        if word[int(index)] != secret_word[int(index)]:
                            add_to_list = False
                    for index in range(len(guessed_word)):
                        if index !=int(index_guessed[0]) and word[index] == secret_word[int(index_guessed[0])]:
                            add_to_list = False
                    if add_to_list:
                        word_base.append(word)
    f.close()

#function that returns a strin of indices for matching character 
def create_index_list(secret_word, letter_guessed):
    index_list= []
    for index in range(len(secret_word)):
        if secret_word[index] == letter_guessed:
            index_list.append(index)
    return index_list

#checks new_word 
def check_new_word(secret_word, letters_guessed, new_word):
    if len(secret_word) != len(new_word):
        return True
    for index in range(len(secret_word)):
        if secret_word[index] in letters_guessed:
            if new_word[index] != secret_word[index]:
                return True
    for letter in new_word:
        if letter in letters_guessed:
            if letter in secret_word:
                pass
            else:
                return True
    return False

#function that changes the secret_word to a random word
def randomize_word(secret_word, letters_guessed):
    for words in word_base:
        if check_new_word(secret_word, letters_guessed, words) == False:
            return words
    else:
        return secret_word


#function that checks if the whole word is guessed
def is_word_guessed(secret_word, letters_guessed):
    for letters in secret_word:
        if letters in letters_guessed:
            pass
        else:
            return False
    return True
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

#function that makes a string of guess for user with __s
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word += letters
        else: 
            guessed_word += '_'
    return guessed_word
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet


# function that checks if guessed letter is in secret word
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
  
    guesses = len(secret_word)  #number of guesses player has left
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
            print("Test: " + secret_word )
            if len(word_base) == 0:
                create_word_base(secret_word, create_index_list(secret_word, guess))
            secret_word = randomize_word(secret_word, letters_guessed)
            print("new secret word: " + secret_word)
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
playing = True
while playing == True:
    playing = False
    os.system('clear')
    secret_word = load_word()
    spaceman(load_word())
    if input("Would you like to play again?(Y/N)") in "Yy":
        playing = True
    else:
        print("Have a good day!")
