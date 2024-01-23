from text import to_upper, to_word_list_isupper
import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')





if __name__ == '__main__':
    unittest.main()
