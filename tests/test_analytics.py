import pytest
from src.analytics.engine import FinancialAnalyticsEngine


def test_moving_average_calculation_precision():
    """Verify that the engine converts raw history arrays and accurately outputs rolling averages."""
    # Mocking 5 days of real stock historical shape data
    mock_history = {
        "2026-06-01": {"4. close": "100.00"},
        "2026-06-02": {"4. close": "102.00"},
        "2026-06-03": {"4. close": "104.00"},
        "2026-06-04": {"4. close": "106.00"},
        "2026-06-05": {"4. close": "108.00"},
    }

    # Run our calculation engine with a window size of 5 days
    processed_df = FinancialAnalyticsEngine.calculate_moving_average(
        mock_history, window_size=5
    )

    # Assertions to ensure math precision
    # The mathematical average of [100, 102, 104, 106, 108] is exactly 104.00
    last_row_calculated_avg = processed_df["moving_avg"].iloc[-1]

    assert last_row_calculated_avg == 104.00
