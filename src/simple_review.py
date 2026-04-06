import pandas as pd

# Defines the columns to include for extraction from the csv file 
simple_bucket = ["rating", "status", "job", "title"]

def satisfaction(rating): 
    """Converts the star rating to a percentage."""
    return int((rating/5.0) * 100)

def happiness(rating): 
    """Returns a string based on the employee's star rating."""
    if rating < 2: 
        return "unhappy"
    elif rating == 3: 
        return "neutral"
    else: 
        return "happy"

class SimpleReview: 
    """Represents a condensed version of a review."""
    def __init__(self, rating, status, job, title):
        self.rating = rating
        self.status = status
        self.job = job 
        self.title = title
        self.summary = None

    def set_summary(self, summary_type): 
         """Sets the type of summary to be displayed with the review."""
         self.summary = summary_type
    
    def get_summary(self): 
        """Returns a summary of the overall review."""
        if self.summary == "satisfaction":
            return satisfaction(self.rating)
        elif self.summary == "happiness": 
            return happiness(self.rating)
        else:
            return self.title       # return the review title by default 
    
    def display_review(self): 
        """Prints the simple review in a readable format."""
        print("------------------------------------------------------------")
        print(f"{self.rating}/5.0\n")
        print(self.get_summary())
        print(f"\t{self.job}\n")
        print(f"\t({self.status})\n")


if __name__ == "__main__": 
    # Reading first 50 because the data is very large 
    df = pd.read_csv("./data/all_reviews.csv", usecols=simple_bucket, nrows=50)

    # Put all reviews into a list 
    simple_reviews = [] 
    for row in df.itertuples(index=False): 
        review = SimpleReview(row.rating, row.status, row.job, row.title)
        simple_reviews.append(review)

    # Testing 
    assert(len(simple_reviews) == 50)
