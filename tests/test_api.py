import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.api import app

client = TestClient(app)


def test_health_endpoint_status_and_payload():
    """Verify that the system health gateway returns a standard HTTP 200 and valid tracking JSON."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "alphapulse-core"}


@patch("src.services.market_data.MarketDataService.get_historical_daily")
@patch("src.services.ai_agent.FinancialAgentService.generate_market_report")
def test_analyze_endpoint_returns_structured_matrix(mock_ai, mock_market):
    """Verify that the analysis endpoint executes cleanly using mocked data dependencies to prevent rate limits."""

    # 1. Simulate a mock historical dictionary from Alpha Vantage
    mock_market.return_value = {
        "2026-07-03": {
            "1. open": "100.0",
            "2. high": "105.0",
            "3. low": "99.0",
            "4. close": "101.0",
            "5. volume": "1000",
        },
        "2026-07-04": {
            "1. open": "101.0",
            "2. high": "106.0",
            "3. low": "100.0",
            "4. close": "102.0",
            "5. volume": "1100",
        },
        "2026-07-05": {
            "1. open": "102.0",
            "2. high": "107.0",
            "3. low": "101.0",
            "4. close": "103.0",
            "5. volume": "1200",
        },
        "2026-07-06": {
            "1. open": "103.0",
            "2. high": "108.0",
            "3. low": "102.0",
            "4. close": "104.0",
            "5. volume": "1300",
        },
        "2026-07-07": {
            "1. open": "104.0",
            "2. high": "109.0",
            "3. low": "103.0",
            "4. close": "105.0",
            "5. volume": "1400",
        },
    }

    # 2. Simulate a mock string response from the Groq AI agent
    mock_ai.return_value = "Mocked Wall Street Analysis: Asset displays a bullish momentum structural configuration."

    # 3. Hit the live local test client route
    response = client.get("/analyze/msft")

    # 4. Assertions
    assert response.status_code == 200
    data = response.json()
    assert data["ticker"] == "MSFT"
    assert data["date"] == "2026-07-07"
    assert data["metrics"]["close_price"] == 105.0
    assert data["metrics"]["signal"] == "BULLISH"
    assert "Mocked Wall Street Analysis" in data["analysis_report"]
