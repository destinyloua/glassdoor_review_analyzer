import sys 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from simple_review import SimpleReview, happiness, satisfaction
import pandas as pd
import unittest

r1 = SimpleReview(4, 'Current Employee', 'Manager', 'Great place to work.')


class TestSimpleReview(unittest.TestCase): 
    def setUp(self): 
        """Initializes test class with mock data."""
        self.sr = r1

    def test_happiness(self): 
        """Tests that the happiness function correctly returns 'happy' for a 4 star rated review."""
        expected = 'happy'
        actual = happiness(self.sr.rating)
        self.assertEqual(expected, actual)

    def test_satisfaction(self): 
        """Tests that the satisfaction function correctly returns 80 (%) for a 4/5 star review."""
        expected = 80 
        actual = satisfaction(self.sr.rating)
        self.assertEqual(expected, actual)

    def test_summary_satisfaction(self): 
        """Tests that the summary type is changed to 'satsfaction'."""
        self.sr.set_summary('satisfaction')
        expected = satisfaction(self.sr.rating)
        actual = self.sr.get_summary() 
        self.assertEqual(expected, actual)

    def test_summary_happiness(self): 
        """Tests that the summary type is changed to 'happiness'."""
        self.sr.set_summary('happiness')
        expected = happiness(self.sr.rating)
        actual = self.sr.get_summary() 
        self.assertEqual(expected, actual)


if __name__ == "__main__": 
    unittest.main()  

