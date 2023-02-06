import random

def find_longest_string(filename):

    with open(filename, 'r') as file:
        words = file.readlines()

    # creates a list of all words from the text file
    words = [word.strip() for word in words]

    # creates a list of 7 random words from the previously created list
    random_words = random.sample(words, 7)

    longest_string = random_words[0]
    for string in random_words:
        # checks if len of current word is longer than current longest word, if so longest word is replaced
        if len(string) > len(longest_string):
            longest_string = string
    
    return longest_string

print(find_longest_string("words.txt"))
