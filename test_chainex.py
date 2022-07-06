# unit test
import corechainex
import unittest
import datetime as dt
testPhrase = "A Brown Fox Jumped Over The Lazy Dogs quickly!" # Random phrase including all alphabet
class ChainexTest (unittest.TestCase):

    def test_encrypt_modes(self):
        # Tests for Encryption Modes
        self.assertIsNotNone(corechainex.encrypt(testPhrase, 1, "0", "")[0], "No result encryption expected. MODE =  0 (minutes)")
        self.assertIsNotNone(corechainex.encrypt(testPhrase, 1, "0", "")[0], "No result encryption expected. MODE =  1 (hours)")
        self.assertIsNotNone(corechainex.encrypt(testPhrase, 1, "2", "")[0], "No result encryption expected. MODE =  2 (days)")
        self.assertIsNotNone(corechainex.encrypt(testPhrase, 1, "3", "")[0], "No result encryption expected. MODE =  3 (months)")
        self.assertIsNotNone(corechainex.encrypt(testPhrase, 1, "4", "")[0], "No result encryption expected. MODE =  4 (years)")
    
    def test_returned_values(self):
        # Tests for Values returned (quantity)
        self.assertEqual(len(corechainex.encrypt(testPhrase, 1, "1", "")), 1, "Two values given, 1 expected")
        self.assertEqual(len(corechainex.encrypt(testPhrase, 1, "1", "I want 2 values")), 2, "1 value given, 2 expected")
        
    def test_encrypt_and_decrypt_minute(self):  
        # Tests for Encrypting and decrypting  
        for mode in range(5): # loop through 4 different modes (min, hours, days, months, years) --> 0,1,2,3,4
            for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890!"·$%&/()=':
                # Repeated test with different chars (not all)
                result = corechainex.encrypt(str(letter), 1, "1", "")
                self.assertEqual([str(letter)], corechainex.encrypt(result, 2, str(mode), ""), "encrypt & decrypt. Did not work with {letter}. In Mode nº {mode}".format(letter=letter, mode=mode))


if __name__ == "__main__":
    unittest.main()