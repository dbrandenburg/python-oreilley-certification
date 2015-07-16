#!/usr/bin/env python3

import unittest
import ccn_safety2

class TestAnonymize(unittest.TestCase):
    
    def test_sample_text(self):
       self.assertEqual("Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and security experts.", ccn_safety2.anonymize(), 'Wrong start and end position returned')
    
if __name__ == "__main__":
    unittest.main()