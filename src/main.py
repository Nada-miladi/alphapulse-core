import sys
from src.services.market_data import MarketDataService
from src.analytics.engine import FinancialAnalyticsEngine
from src.services.ai_agent import FinancialAgentService


def run_alpha_pulse_analysis(ticker: str):
    """
    Coordinates the entire data-to-intelligence pipeline:
    1. Fetches historical stock data
    2. Computes the 5-day Simple Moving Average (SMA)
    3. Triggers the Llama-3.1 AI agent for expert commentary
    """
    print(
        f"\n[INFO] Initializing AlphaPulse Core Analysis Engine for Asset: {ticker}..."
    )

    # 1. Initialize our services
    market_service = MarketDataService()
    analytics_engine = FinancialAnalyticsEngine()
    ai_agent = FinancialAgentService()

    try:
        # 2. Fetch raw historical daily data from Alpha Vantage
        print(f"[INFO] Querying live market historical data streams...")
        raw_history = market_service.get_historical_daily(ticker)

        # 3. Compute mathematical moving averages via Pandas
        print(f"[INFO] Running time-series numeric analytical operations...")
        processed_df = analytics_engine.calculate_moving_average(
            raw_history, window_size=5
        )

        # 4. Extract the latest metrics to pass to our AI
        latest_row = processed_df.iloc[-1]
        latest_date = processed_df.index[-1].strftime("%Y-%m-%d")
        latest_close = latest_row["close"]
        latest_sma = latest_row["moving_avg"]

        signal = (
            "BULLISH (Trading above SMA)"
            if latest_close >= latest_sma
            else "BEARISH (Trading below SMA)"
        )

        analytics_summary = (
            f"As of Date: {latest_date} | "
            f"Last Closing Price: ${latest_close:.2f} | "
            f"5-Day Simple Moving Average: ${latest_sma:.2f} | "
            f"Automated Signal: {signal}."
        )

        # 5. Pipe the clean numbers directly into the AI engine via Groq LPU
        print(
            f"[INFO] Dispatching quantitative report matrix to high-speed AI Agent..."
        )
        ai_report = ai_agent.generate_market_report(
            ticker=ticker, analytics_summary=analytics_summary
        )

        # 6. Print the clean corporate format final product
        print(
            "\n====================================================================================="
        )
        print(f"ALPHAPULSE EXECUTIVE MARKET INTELLIGENCE REPORT FOR: {ticker}")
        print(
            "====================================================================================="
        )
        print(ai_report)
        print(
            "=====================================================================================\n"
        )

    except Exception as e:
        print(
            f"[ERROR] Critical Pipeline Failure during orchestration run: {str(e)}",
            file=sys.stderr,
        )


if __name__ == "__main__":
    target_asset = sys.argv[1].upper() if len(sys.argv) > 1 else "AAPL"
    run_alpha_pulse_analysis(target_asset)
