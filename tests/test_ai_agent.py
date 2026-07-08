import pytest
from src.services.ai_agent import FinancialAgentService


def test_ai_agent_generates_valid_financial_analysis():
    """Verify that the AI Agent successfully communicates with Groq and returns analytical commentary."""
    agent = FinancialAgentService()

    mock_analytics_data = (
        "Date: 2026-06-19 | Close Price: $421.90 | 5-Day Simple Moving Average: $418.50 | "
        "Trend Signal: Asset is trading above its moving average (Bullish Momentum)."
    )

    report = agent.generate_market_report(
        ticker="MSFT", analytics_summary=mock_analytics_data
    )

    assert report is not None
    assert len(report) > 0
    assert isinstance(report, str)
