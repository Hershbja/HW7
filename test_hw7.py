import unittest
import HW7 as q

class TestCase(unittest.TestCase):
    def test_FizzBuzz(self):
        result = def FizzBuzz(15)
        self.assertEqual(result, "FizzBuzz")
        
        result = def FizzBuzz(18)
        self.assertEqual(result, "Fizz")
        
        result = def FizzBuzz(25)
        self.assertEqual(result, "Buzz")
        
        result = def FizzBuzz(17)
        self.assertEqual(result, 17)

if __name__ == '__main__':
    unittest.main()