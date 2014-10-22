#!/usr/bin/env python3

import unittest
import shelve
import os
import highscore

class TestHighscore(unittest.TestCase):
    """Testing of the highscore funcion"""
    
    def setUp(self):
        """Setup highscore vars and shelve"""
        self.playername = "Dennis"
        score = 2
        self.db = "tmp"
        shelf = shelve.open(self.db)
        shelf[self.playername] = score
        shelf.close()

    def test_new_user(self):
        """Testing highscore for new user"""
        score = 2
        playername = "Mike"
        current_highscore = highscore.highscore(playername,score,self.db)
        self.assertEqual( 2, current_highscore, 'Should return the same score as passed')
        
    def test_same_score(self):
        """Testing highscore for new user"""
        score = 2
        current_highscore = highscore.highscore(self.playername,score,self.db)
        self.assertEqual( 2, current_highscore, 'Should return the same score as passed')
        
    def test_lower_score(self):
        """Testing highscore for existing user with lower value existent"""
        score = 1
        current_highscore = highscore.highscore(self.playername,score,self.db)
        self.assertEqual( 2, current_highscore, 'Schould return the existent value rather than the given parameter')
        
    def test_higher_score(self):
        """Testing highscore for existing user with higher value than existent"""
        score = 3
        current_highscore = highscore.highscore(self.playername,score,self.db)
        self.assertEqual( 3, current_highscore,'Should return the as a parameter given score')
        
    def tearDown(self):
        """Ramp down highscore vars and shelve"""
        os.remove(self.db + ".db")   
    
if __name__ == "__main__":
    unittest.main()