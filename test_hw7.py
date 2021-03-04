import unittest
import hw7 as q

class TestCase(unittest.TestCase):
    def test_FizzBuzz(self):
        result = q.FizzBuzz(15)
        self.assertEqual(result, "FizzBuzz")
        
        result = q.FizzBuzz(18)
        self.assertEqual(result, "Fizz")
        
        result = q.FizzBuzz(25)
        self.assertEqual(result, "Buzz")
        
        result = q.FizzBuzz(17)
        self.assertEqual(result, 17)

if __name__ == '__main__':
    unittest.main()