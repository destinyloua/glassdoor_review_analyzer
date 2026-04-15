import pandas as pd



class ReviewAnalyzer:
    """Analyze a DataFrame of simplified Glassdoor reviews."""

    def __init__(self, dataframe: pd.DataFrame):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("dataframe must be a pandas DataFrame")

        if dataframe.empty:
            raise ValueError("dataframe cannot be empty")

        self.dataframe = dataframe.copy()

    def review_count(self) -> int:
        """Return the total number of reviews."""
        return len(self.dataframe)

    def average_rating(self, rating_column: str = "overall_rating") -> float:
        """Return the average overall rating."""
        self._check_column(rating_column)

        ratings = pd.to_numeric(self.dataframe[rating_column], errors="coerce").dropna()
        if ratings.empty:
            raise ValueError(f"'{rating_column}' has no numeric values")

        return float(ratings.mean())

    def descriptive_statistics(self, rating_column: str = "overall_rating") -> dict:
        """Return descriptive statistics for a rating column."""
        self._check_column(rating_column)

        ratings = pd.to_numeric(self.dataframe[rating_column], errors="coerce").dropna()
        if ratings.empty:
            raise ValueError(f"'{rating_column}' has no numeric values")

        return {"count": int(ratings.count()),
                "mean": float(ratings.mean()),
                "median": float(ratings.median()),
                "min": float(ratings.min()),
                "max": float(ratings.max()),
                "std": float(ratings.std())}

    def bucket_ratings(
        self,
        rating_column: str = "overall_rating",
        bucket_column: str = "rating_bucket"
    ) -> pd.DataFrame:
        """
        Create rating buckets:
        low    : < 2.5
        medium : 2.5 to < 4.0
        high   : >= 4.0
        """
        self._check_column(rating_column)

        df = self.dataframe.copy()
        ratings = pd.to_numeric(df[rating_column], errors="coerce")

        df[bucket_column] = pd.cut(
            ratings,
            bins=[-float("inf"), 2.5, 4.0, float("inf")],
            labels=["low", "medium", "high"],
            right=False
        )

        return df

    def group_average(
        self,
        group_column: str,
        rating_column: str = "overall_rating"
    ) -> pd.DataFrame:
        """Return the average rating grouped by a selected column. 
        Example group columns: company_name, job_title, location"""
        self._check_column(group_column)
        self._check_column(rating_column)

        df = self.dataframe.copy()
        df[rating_column] = pd.to_numeric(df[rating_column], errors="coerce")

        result = (
            df.groupby(group_column, dropna=False)[rating_column]
            .mean()
            .reset_index(name="average_rating")
            .sort_values(by="average_rating", ascending=False)
        )

        return result

    def bucket_counts(
        self,
        rating_column: str = "overall_rating"
    ) -> pd.Series:
        """Return the number of reviews in each rating bucket."""
        bucketed_df = self.bucket_ratings(rating_column=rating_column)
        return bucketed_df["rating_bucket"].value_counts(dropna=False)

    def _check_column(self, column: str) -> None:
        """Check whether the column exists in the DataFrame."""
        if column not in self.dataframe.columns:
            raise KeyError(f"column '{column}' not found in dataframe")
    
    
    
