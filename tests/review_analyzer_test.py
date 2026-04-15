import pandas as pd
import unittest

# Import the class we want to test
from src.review_analyser import ReviewAnalyzer


class TestReviewAnalyzer(unittest.TestCase):

    def setUp(self):
        """Create a small sample DataFrame for testing. This runs before each test method."""
        self.df = pd.DataFrame({
            "company_name": ["A", "B"],
            "overall_rating": [4.0, 2.0],
        })
        self.analyzer = ReviewAnalyzer(self.df)

    def test_review_count(self):
        """Check if the total number of reviews is correct."""
        self.assertEqual(self.analyzer.review_count(), 2)

    def test_average_rating(self):
        """Check if the average rating is calculated correctly."""
        self.assertEqual(self.analyzer.average_rating(), 3.0)

    def test_bucket_column_exists(self):
        """Check if bucket_ratings adds a new column 'rating_bucket'."""
        result = self.analyzer.bucket_ratings()
        self.assertIn("rating_bucket", result.columns)

    def test_invalid_column(self):
        """Check if using an invalid column raises an error."""
        with self.assertRaises(KeyError):
            self.analyzer.average_rating("wrong")


# Run tests when this file is executed directly
if __name__ == "__main__":
    unittest.main()