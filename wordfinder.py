# This is a simple word game.
# The program will select a random word with 7 unique letters from a dictionary.
# Then, it will select a random letter from this word to be the required letter.
# The player must find as many words as possible that can be formed from the given letters,
# including the required letter, and are at least 4 letters long.
# This uses the words file from Unix - https://en.wikipedia.org/wiki/Words_(Unix)

# import the random module
import random

# function to create a list of possible words
def create_word_list(words, word, letter):
    # find how many words can be made from the letters in the random word which also contain the random letter
    possible_words = set()
    # limit the words to those with 4 or more letters
    word_list = [word for word in words if len(word) >= 4]
    # check if each word contains the required letter and is made up of only letters from the random word
    for i in word_list:
        # only check words with the required letter
        if letter in i.lower():
            # check if all the letters in the word exist in the subset of letters from the selected word
            if set(i.lower()).issubset(set(word.lower())):
                # add to the word set
                possible_words.add(i)
    # return the list of words
    return possible_words

# function to generate a random word with 7 unique letters
def generate_word(words):
    # create a list of words with 7 unique letters
    seven_unique_letter_words = [word for word in words if len(set(word)) == 7]
    # choose a random word from this list to be the baseline word for the game
    return random.choice(seven_unique_letter_words)

# function to validate the input from the user
def validate_word(word):
    # check if the word is at least 4 letters long
    if len(word) < 4:
        return False
    # check if the word contains only alphabetic characters
    if not word.isalpha():
        return False
    return True

# main function to run the game
def main():
    # read the word list using the linux dictionary
    with open('linuxwords.txt', 'r') as f:
        words = f.read().splitlines()
    # remove proper nouns
    words = [word for word in words if word.islower()]

    # generate a random word
    random_word = generate_word(words)
    # choose a random letter from the word 
    random_letter = random.choice(random_word)
    # create the list of possible words using the word list, random word, and random letter 
    possible_words = create_word_list(words, random_word, random_letter)

    # let the game begin! create an empty set to hold found words
    foundWords = set()
    # create a variable to hold the unique letters of the word for shuffling
    shuffled = list(set(random_word))

    print('Welcome to the Word Finder Game! Type \'quit!\' to exit, or \'shuffle!\' to mix up the letters.')

    # main game loop, run while there are still words to find
    while(len(foundWords) < len(possible_words)):
        print('')
        print('Here are the random letters: ', ' '.join(shuffled))
        print('The required letter is: ', random_letter)
        print(f'There are {len(possible_words) - len(foundWords)} words left to find.')
        print('')
        # get the user's input
        chosenWord = input('Enter a word: ')
        # handle shuffling the letters
        if chosenWord.lower() == 'shuffle!':
            print(f'Shuffling the letters...')
            random.shuffle(shuffled)
            continue
        # handle exiting the game
        if chosenWord.lower() == 'quit!':
            break
        # otherwise, check the word
        if not validate_word(chosenWord.lower()):
            print('Please enter a word with at least 4 letters.')
            continue
        response = ''
        if chosenWord.lower() in possible_words:
            # if the word has already been found, don't count it again
            if chosenWord.lower() in foundWords:
                print(f'You already found {chosenWord}!')
                continue
            # if the word contains all the letters in the random word, celebrate
            if set(random_word).issubset(set(chosenWord.lower())):
                response = 'Incredible! You found a pangram!'
            else:
                response = 'Good job!'
            foundWords.add(chosenWord.lower())
        else:
            response = 'Sorry, that word is not valid.'
        print(f'{response} You have found {len(foundWords)} word{"s" if len(foundWords) != 1 else ""} so far.')
        print('Words found: ', ', '.join(foundWords))

    # use a special message if all words are found
    if len(foundWords) == len(possible_words):
        print('You found every word! Congratulations!')

    # end with the starting word and all possible words    
    print(f'The selected word was: {random_word}.')
    print(f'The possible words were: {", ".join(sorted(possible_words))}.')

if __name__ == '__main__':

    main()

