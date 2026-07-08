import httpx
from src.core.config import settings


class MarketDataService:
    def __init__(self):
        self.api_key = settings.ALPHA_VANTAGE_API_KEY
        self.base_url = "https://www.alphavantage.co/query"
        # Set a professional 15-second timeout pool for network requests
        self.timeout = httpx.Timeout(15.0, connect=5.0)

    def get_live_price(self, symbol: str) -> dict:
        """Fetches the global quote (real-time price data) for a given stock symbol."""
        params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": self.api_key}
        response = httpx.get(self.base_url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        if "Global Quote" not in data or not data["Global Quote"]:
            raise ValueError(
                f"Could not fetch valid market data for symbol: {symbol}. Response: {data}"
            )
        return data["Global Quote"]

    def get_historical_daily(self, symbol: str) -> dict:
        """Fetches the daily historical price data (last 100 days) for a given stock symbol."""
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key,
        }
        response = httpx.get(self.base_url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()

        if "Time Series (Daily)" not in data:
            raise ValueError(
                f"Could not fetch historical data for symbol: {symbol}. Response: {data}"
            )

        return data["Time Series (Daily)"]
