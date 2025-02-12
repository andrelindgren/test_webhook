import unittest
from src.myprogram import my_function  # Replace 'your_module' with the actual name of the file where my_function is defined

class TestMyFunction(unittest.TestCase):
    def test_returns_same_text(self):
        """
        Ensure that my_function returns exactly the text passed to it.
        """
        input_text = "Hello World"
        output_text = my_function(input_text)
        self.assertEqual(output_text, input_text, "it should have worked!")

    def test_empty_string(self):
        """
        Edge case: empty string should return empty string.
        """
        self.assertEqual(my_function(""), "")

if __name__ == "__main__":
    unittest.main()
