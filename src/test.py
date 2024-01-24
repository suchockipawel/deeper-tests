from text import to_upper, to_word_list_isupper
import unittest
from app import rnd, max_num_in_list, rm
from unittest.mock import patch


# Section 1 (Basic Assert Methods)

''' Task1
# Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will return the `"ABCDEF"` when called with the argument "abcdef"'''

class TestToUpperFunction(unittest.TestCase):

    def test_upper_conversion(self):
        input_str = "abcdef"
        expected_output = "ABCDEF"
        result = to_upper(input_str)
        self.assertEqual(result, expected_output)

'''Task2 & Task3
# Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `True` when called with the argument `['I', 'LOVE', 'YOU']`.

# Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will return `False` when called with the argument `['i', 'LOVE', 'YOU']`.
'''

class TestToWordListIsUpperFunction(unittest.TestCase):

    def test_all_uppercase_words(self):
        input_list = ['I', 'LOVE', 'YOU']
        self.assertTrue(to_word_list_isupper(input_list))

    def test_contains_lowercase_word(self):
        input_list = ['i', 'LOVE', 'YOU']
        self.assertFalse(to_word_list_isupper(input_list))


''' Task4
# Write a test in `src/test.py` to check if the function `to_upper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a string (**str**).'''

class TestToUpperCaseFunction(unittest.TestCase):

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            to_upper(123) # Pass an integer as a non-string argument

''' Task5
# Write a test in `src/test.py` to check if the function `to_word_list_isupper` in `src/text.py` will raise a **TypeError** if called with an argument that is not a **list**.'''

class TestToWordListIsUpperFunction(unittest.TestCase):

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper("Not a list")  # Pass a string as a non-list argument


# Section 2 (Unittest Basic 2: More Assert Methods)

'''Task 1 & Task 2

Write a test to check if the function `rnd` in `src/app.py` will return the correct value given these arguments: `start = 2` and `end = 20`.
Write a test to check if the function `rnd` in `src/app.py` will not return an out-of-range value given these arguments: `start = 2` and `end = 20`'''

class TestRndFunction(unittest.TestCase):

    def test_within_range(self):
        start = 2
        end = 20
        result = rnd(start, end)
        self.assertTrue(start <= result <= end)

    def test_no_out_of_range_value(self):
        start = 2
        end = 20
        result = rnd(start, end)
        self.assertFalse(result < start or result > end)

'''Task 3
What problem is there with testing a method that involves randomized value? Can we be sure that the test passes every time when it has passed once? Add a code comment to the tests of task 1 and 2 about any potential issues with those tests.'''

# When testing methods that involve randomized values, there are certain challenges related to the unpredictability of the output. 
# The key problem is that the randomness of the 'rnd' function may lead to intermittent test failures, even when the function is working correctly.# Testing random values introduces non-determinism.
# It's advisable to use statistical methods or multiple runs to gain confidence.

'''Task 4

Fix the function `max_num_in_list` in `src/app.py`. It should return the highest number of the list of numbers given as the argument. That way it will pass the test.'''


class TestApp(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')

# Section 3 (Unittest Mocking)

'''Task1
Write a test to check if the `rm` function in `src/app.py` will delete a file.'''


class TestRemoveFunction(unittest.TestCase):

    def test_remove_file(self):
        test_filename = "test_file.txt"
        with open(test_filename, 'w') as test_file:
            test_file.write("Test content")

        self.remove_file(test_filename)

        self.assertFalse(os.path.exists(test_filename))


'''Task2

Write a test to check if the `rm` function in `src/app.py` will call the `os.remove` function if the file exists - without deleting the file. Use `unittest.mock` for this purpose.'''

class TestRemoveFunction(unittest.TestCase):

    @patch('os.remove')
    def test_call_os_remove(self, mock_remove):
        test_filename = "test_file.txt"
        with open(test_filename, 'w') as test_file:
            test_file.write("Test content")

        rm(test_filename)

        mock_remove.assert_called_once_with(test_filename)

'''Task3
Write a test to make sure that the `rm` function in `src/app.py` will **NOT** call the `os.remove` function if the file **DOES NOT** exist. Use `unittest.mock` for this purpose.'''

class TestRemoveFunction(unittest.TestCase):

    @patch('os.remove')  
    def test_do_not_call_os_remove(self, mock_remove):
        rm("non_existing_file.txt")

        mock_remove.assert_not_called()

'''Task4
Fix the `rm` function in `src/app.py` so that it will raise a **FileNotFoundError** error if the file does not exist.'''

'''Task5
Write a test to check if the `rm` function in `src/app.py` will raise a **FileNotFoundError** error if the file **DOES NOT** exist. Use `unittest.mock` for this purpose.'''

class TestRemoveFunction(unittest.TestCase):

    @patch('os.remove')
    def test_raise_file_not_found_error(self, mock_remove):
        mock_remove.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            rm("non_existing_file.txt")

        mock_remove.assert_called_once_with("non_existing_file.txt")


if __name__ == '__main__':
    unittest.main()
