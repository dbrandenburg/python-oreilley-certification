#!/usr/bin/env python3

import unittest
import ccn_safety2

class TestAnonymize(unittest.TestCase):
    
    def test_sample_text(self):
        test_string = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake" \
        " numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as" \
        " 1234-5678-1234-5678, triggers the attention of privacy and security experts."
        self.assertEqual("Have you ever noticed, in television and movies, that phone numbers and credit cards are" \
        " obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number that appears to be " \
        "real, such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and security experts.", 
       ccn_safety2.anonymize(test_string), 'Wrong start and end position returned')
    
if __name__ == "__main__":
    unittest.main()