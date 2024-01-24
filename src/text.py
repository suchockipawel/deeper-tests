
'''Task6
Fix both functions to_upper and to_word_list_isupper in src/text.py so they will raise a TypeError if the argument was not the right type (string in the case of to_upper and list in the case of to_word_list_upper).'''


# function will convert string parameter to upper case
#def to_upper(str):
#    return str.upper()

# function will check return true if all items on
# the parameter list are upper case
#def to_word_list_isupper(str_list):
#    for word in str_list:
#        if word.islower():
#            return False
#    return True



def to_upper(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    return input_str.upper()

def to_word_list_isupper(str_list):
    if not isinstance(str_list, list):
        raise TypeError("Input must be a list")
    
    for word in str_list:
        if not isinstance(word, str):
            raise TypeError("Elements in the list must be strings")
        if word.islower():
            return False
    return True