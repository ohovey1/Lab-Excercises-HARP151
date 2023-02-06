
list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]

def find_longest_string(string_list):

    longest_string = string_list[0]
    for string in list:
        # checks if len of current word is longer than current longest word, if so longest word is replaced
        if len(string) > len(longest_string):
            longest_string = string
    
    return longest_string

print(find_longest_string(list))
