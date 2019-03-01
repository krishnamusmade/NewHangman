# Problem Set 2, hangman.py
# Name:Krishna Vijay Musmade
# Collaborators:
# Time spent:3 days

# Hangman Game
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in;
    False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
    which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for char in secret_word:
        if char not in letters_guessed:
            guessed_word += '_ '
        else:
            guessed_word += char
    return guessed_word


def get_available_letters(letters_guessed):
    # '''
    # letters_guessed: list (of letters), which letters have been guessed so
    # returns: string (of letters), comprised of letters that represents which
    #   yet been guessed.
    # '''

    abc = string.ascii_lowercase
    for i in range(len(letters_guessed)):
        abc = abc.replace(letters_guessed[i], "")

    return abc


def print_end_game_message(guesses, secret_word):
    '''
    # guesses_remaining: int, the number of guesses remaining (at the end of)
    secret_word: string, the word the user was guessing
    returns: None
    prints a message for the user at the end of the game with their score if 
    and with the secret_word if they did not win
    '''
    def total_score(guesses, secret_word):
        '''
        guesses_remaining: int, the number of guesses remaining (at the end)
        secret_word: string, the word the user was guessing
        returns: int, the total score associated with the winning game
        '''
        unique_secret_word = ''
        for char in secret_word:
            if char not in unique_secret_word:
                unique_secret_word += char
        return guesses * len(unique_secret_word)
    if guesses > 0:
        print('Congratulations, you won!')
        print('Your total score for this game is:',
              total_score(guesses, secret_word))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word + ".")


def warn(warning, guess):
    if warning <= 0:
        guess -= 1
        print('\nYou have no warnings left so you loose one guess!!')
        return guess
    else:
        warning -= 1
        print('\nPlease enter a valid character!!')
        return warning


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses = 6
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    guessed_word = ''
    guess_word = []
    '''
        letters_guessed: list (of letters), which letters have been guessed so
         returns: string (of letters), comprised of letters that represents
         yet been guessed.
        '''
    if letters_guessed == []:
        return string.ascii_lowercase
    else:
        available_letters = ''
        for char in string.ascii_lowercase:
            if char not in letters_guessed:
                available_letters += char
        return available_letters
    print('\nYou have ', warnings, 'warnings and', guesses, 'guesses')
    secret_word = choose_word(wordlist)
    lengthword = len(secret_word)
    print('\nThe length of the secretword is', lengthword)
    for char in secret_word:
        guess_word.append('_')
    print(guess_word)
    print()
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        if guesses == 1:
            print('\nYou have', guesses, 'guess left')
        else:
            print('\nYou have', guesses, 'guesses left')
        print('\nAvailable letters:- ', get_available_letters(letters_guessed))
        letter_guessed = str.lower(input('Please guess a letter: '))
        is_char_invalid = not str.isalpha(letter_guessed)
        is_letter_already_taken = letter_guessed in letters_guessed
        if is_char_invalid:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left so you loose one guess!!')
            else:
                warnings -= 1
            print('\nPlease enter a one character')
            print('\nYou have ', warnings, 'warnings left.')
        elif is_letter_already_taken:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left so you loose one guess!!')
            else:
                warnings -= 1
            print('\nPlease enter a one character')
            print('\nYou have ', warnings, 'warnings left.')
        else:
            letters_guessed.extend(letter_guessed)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guessed in secret_word:
                print('Good guess:', guessed_word)
            else:
                if letter_guessed in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                print('Oops! That letter is not in secret word:', guessed_word)
        print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print_end_game_message(guesses, secret_word)


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and (my_word[i] != other_word[i]):
                return False
        return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches
             Keep in mind that in hangman when a letter is guessed, all the
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in
             the word that has already been revealed.

    '''
    words_list = loadwoeds()
    possible_matches = []
    for other_word in words_list:
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
    print(' '.join(possible_matches))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the
     guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses = 6
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    guessed_word = ''
    guess_word = []
    print('\nYou have ', warnings, 'warnings and', guesses, 'guesses')
    secret_word = choose_word(wordlist)
    lengthword = len(secret_word)
    print('\nThe length of the secretword is', lengthword)
    for char in secret_word:
        guess_word.append('_')
    print(guess_word)
    print()
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        if guesses == 1:
            print('\nYou have', guesses, 'guess left')
        else:
            print('\nYou have', guesses, 'guesses left')
        print('\nAvailable letters:-', get_available_letters(letters_guessed))
        letter_guessed = str.lower(input('Please guess a letter: '))
        len(letter_guessed)
        is_char_invalid = not str.isalpha(letter_guessed)
        is_letter_already_taken = letter_guessed in letters_guessed
        if len(letter_guessed) > 1:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left so you loose one guess!!')
            else:
                warnings -= 1
            print('\nPlease enter a one character')
            print('\nYou have ', warnings, 'warnings left.')
        elif letter_guessed == '*':
            print('Possible word matches are:-')
            show_possible_matches(guessed_word)
        elif is_char_invalid:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left so you loose one guess!!')
            else:
                warnings -= 1
            print('\nPlease enter a valid character')
            print('\nYou have ', warnings, 'warnings left.')
        elif is_letter_already_taken:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left so you loose one guess!!')
            else:
                warnings -= 1
            print('\nYou have already guessed that letter!!')
            print('\nYou have ', warnings, 'warnings left.')
        else:
            letters_guessed.extend(letter_guessed)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guessed in secret_word:
                print('Good guess:', guessed_word)
            else:
                if letter_guessed in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                print('Oops! That letter is not in secret word:', guessed_word)
        print('\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
    print_end_game_message(guesses, secret_word)


if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    # hangman(secret_word)
    print('\n********Welcome to the game Hangman!!**********')
    name = input('\nEnter your name:-')
    print('\nHello'+name, 'Time to play Hangman')
    # Rules for the game
    print('\nRules For the game are as follows:-\nRule 1:-You have specific number of guesses(If you choose a wrong guess one guess will be deducted).\nRule 2:-You can only enter an alphabets in lower cases.\nRule 3:-You have 3 warnings(If you enter a symbol or number or the same letter 3 times then one guess will be deducted)\nRule 4:-If you guess the letter that has not been guessed before then you losses no guess\nRule 5:-If you wrongly guessed a letter that is consonant then 1 guess will be deducted but if you guess a letter that is vowel and if it is wrong then two guess will be deducted\nRule 6:-Enter * for the hint\nRule 7:-The game will end if you have guessed the right letter or you have ran out of guesses')
    print('\nLets start the game!!')
    hangman_with_hints(secret_word)
