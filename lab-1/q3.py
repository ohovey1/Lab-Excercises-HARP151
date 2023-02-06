##########################################################
## Here are just a few built in methods of dictionaries.##
## There are certainly many others, but these are just ###
## a few examples. #######################################
##########################################################


dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

# gets a list of the keys in the dictionary
keys = dict.keys()
print(keys)

# gets a list of the values in the dictionary
values = dict.values()
print(values)

# returns the value of a specified key
value = dict.get(2)
print(value)

# clears all contents of the dictionary
dict.clear()
print(dict)
