import pytest
from src.services.market_data import MarketDataService


def test_fetch_live_stock_price_successfully():
    """Verify that the MarketDataService connects to Alpha Vantage and returns price data."""
    service = MarketDataService()

    # Let's request real-time data for Microsoft
    raw_data = service.get_live_price("MSFT")

    # Assertions to ensure the data structure matches Alpha Vantage specifications
    assert "01. symbol" in raw_data
    assert raw_data["01. symbol"] == "MSFT"
    assert "05. price" in raw_data

    # Ensure the price field contains an actual positive number represented as a string
    float_price = float(raw_data["05. price"])
    assert float_price > 0.0
