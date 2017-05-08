import unittest
import week12_function as week12


class TestRemoveDupValues(unittest.TestCase):

    def test_empty_dictionary_count(self):
        input_dictionary = dict()
        expected_count = 0
        actual_count = week12.remove_dup_values(input_dictionary)
        message = "Returned number of entries that were removed from an empty\
        dictionary is wrong."
        self.assertEqual(expected_count, actual_count, message)

    def test_empty_dictionary_mutate(self):
        input_dictionary = dict()
        expected_result = dict()
        week12.remove_dup_values(input_dictionary)
        message = "Function doesn't correctly mutate input_dictionary"
        self.assertEqual(expected_result, input_dictionary, message)
    
    def test_single_enetry_dictionary_count(self):
        input_dictionary = {1: 2}
        expected_count = 0
        actual_count = week12.remove_dup_values(input_dictionary)
        message = "Returned number of entries that were removed from a single"
        message += "-entry dictionary is wrong."
        self.assertEqual(expected_count, actual_count, message)
    
    def test_single_entry_dictionary_mutate(self):
        input_dictionary = {1: 2}
        expected_result = {1: 2}
        week12.remove_dup_values(input_dictionary)
        message = "Function doesn't correctly mutate input_dictionary"
        self.assertEqual(expected_result, input_dictionary, message)



if __name__ == "__main__":
    unittest.main(exit=False)
