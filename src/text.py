# function will convert string parameter to upper case
def to_upper(str):
    return str.upper()

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    for word in str_list:
        if word.islower():
            return False
    return True
