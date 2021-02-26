import unittest
from serialkeys import Serialkeys
import time

class SerialkeysTests(unittest.TestCase):

    def test_basic(self):
        generator = Serialkeys()
        keys = generator.generate(10)
        self.assertEqual(len(keys), 10)

    def test_length_OK(self):
        generator = Serialkeys(12)
        keys = generator.generate(1)
        self.assertEqual(len(str(keys[0]).replace("-", "")), 12)

    def test_length_tooshort(self):
        with self.assertRaises(Exception) as context:
            Serialkeys(2)
            self.assertEqual(520, context.exception.code)      

    def test_length_negative(self):
        with self.assertRaises(Exception) as context:
            Serialkeys(-1)
            self.assertEqual(510, context.exception.code)

    def test_chunks_OK(self):
        generator = Serialkeys(12, 3)
        keys = generator.generate(1)
        self.assertEqual(len(str(keys[0]).split("-")), 4)

    def test_chunks_size_1(self):
        generator = Serialkeys(12, 1)
        keys = generator.generate(1)  # No split expected!
        self.assertEqual(len(str(keys[0]).split("-")), 1)

    def test_chunks_size_negative(self):
        with self.assertRaises(Exception) as context:
            Serialkeys(12, -1)
            self.assertEqual(530, context.exception.code)   

    def test_custom_alphabet(self):
        generator = Serialkeys(8, 1, "-", "1234567890")
        keys = generator.generate(1)  
        self.assertEqual(str(keys[0]).isdecimal(), True)

    def test_custom_alphabet_not_diverse(self):
        with self.assertRaises(Exception) as context:
            Serialkeys(8, 1, "-", "123321")
            self.assertEqual(550, context.exception.code)   
            
    def test_custom_alphabet_toosmall(self):
        with self.assertRaises(Exception) as context:
            Serialkeys(8, 2, "-", "12345")
            self.assertEqual(560, context.exception.code)        
            
    def test_toomany_keys_for_alphabet(self):
        with self.assertRaises(Exception) as context:
            Serialkeys(4, 1, "-", "12345")
            self.assertEqual(560, context.exception.code)     

    def test_runtime_OK(self):
        starttime = time.process_time()
        generator = Serialkeys(12)
        generator.generate(10000)
        totaltime = time.process_time() - starttime
        self.assertTrue(totaltime < 1.0)


if __name__ == "__main__":
    unittest.main()
