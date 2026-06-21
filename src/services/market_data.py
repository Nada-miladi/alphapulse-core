import httpx
from src.core.config import settings


class MarketDataService:
    def __init__(self):
        self.api_key = settings.ALPHA_VANTAGE_API_KEY
        self.base_url = "https://www.alphavantage.co/query"

    def get_live_price(self, symbol: str) -> dict:
        """
        Fetches the global quote (real-time price data) for a given stock symbol.
        """
        params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": self.api_key}

        # Make a synchronous HTTP GET request to Alpha Vantage
        response = httpx.get(self.base_url, params=params)
        response.raise_for_status()  # Automatically raise an exception if the internet call fails

        data = response.json()

        # Check if we hit API rate limits or invalid tickers
        if "Global Quote" not in data or not data["Global Quote"]:
            raise ValueError(
                f"Could not fetch valid market data for symbol: {symbol}. Response: {data}"
            )

        return data["Global Quote"]
