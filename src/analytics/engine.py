import pandas as pd


class FinancialAnalyticsEngine:
    @staticmethod
    def calculate_moving_average(
        raw_history: dict, window_size: int = 5
    ) -> pd.DataFrame:
        """
        Converts raw nested historical data into a structured Pandas DataFrame
        and calculates a Simple Moving Average (SMA).
        """
        # 1. Load the raw dictionary data straight into a structured Pandas DataFrame table
        # Rows become dates, columns become the data attributes ('1. open', '4. close', etc.)
        df = pd.DataFrame.from_dict(raw_history, orient="index")

        # 2. Sort dates in ascending order so we calculate moving averages chronologically
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()

        # 3. Extract the closing prices and force them from text/strings to numeric decimals
        df["close"] = pd.to_numeric(df["4. close"])

        # 4. The Magic Step: Use Pandas rolling statistics to calculate our Moving Average instantly
        df["moving_avg"] = df["close"].rolling(window=window_size).mean()

        return df
