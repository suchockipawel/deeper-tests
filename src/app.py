import os
from random import randrange

# function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end+1)

# function should return the greatest number in a list
#def max_num_in_list( list ):
#    max = list[ 0 ]
#    for a in list:
#        if a < max:
#            max = a
#    return max

'''## Task 4

Fix the function `max_num_in_list` in `src/app.py`. It should return the highest number of the list of numbers given as the argument. That way it will pass the test.'''


def max_num_in_list(list):
    if not list:
        return None
    max_num = list[0]
    for a in list:
        if a > max_num:
            max_num = a
    return max_num





# def rm(filename):
#    os.remove(filename)

'''## Task4

Fix the `rm` function in `src/app.py` so that it will raise a **FileNotFoundError** error if the file does not exist.'''

def rm(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")