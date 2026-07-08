from fastapi import FastAPI, HTTPException
from src.services.market_data import MarketDataService
from src.analytics.engine import FinancialAnalyticsEngine
from src.services.ai_agent import FinancialAgentService

# Initialize the master FastAPI application instance
app = FastAPI(title="AlphaPulse Core API", version="1.0.0")

# Initialize our background service infrastructure layers
market_service = MarketDataService()
analytics_engine = FinancialAnalyticsEngine()
ai_agent = FinancialAgentService()


@app.get("/health")
def health_check():
    """Simple verification route to confirm the web server is alive and responding."""
    return {"status": "healthy", "service": "alphapulse-core"}


@app.get("/analyze/{ticker}")
def analyze_asset(ticker: str):
    """
    HTTP GET endpoint that executes the complete quantitative analysis
    and cognitive reporting pipeline for a requested asset symbol.
    """
    symbol = ticker.upper()
    try:
        # 1. Pull data over the network
        raw_history = market_service.get_historical_daily(symbol)

        # 2. Run numerical operations via Pandas
        processed_df = analytics_engine.calculate_moving_average(
            raw_history, window_size=5
        )

        # 3. Sift out our latest matrix row
        latest_row = processed_df.iloc[-1]
        latest_date = processed_df.index[-1].strftime("%Y-%m-%d")
        latest_close = float(latest_row["close"])
        latest_sma = float(latest_row["moving_avg"])

        signal = "BULLISH" if latest_close >= latest_sma else "BEARISH"

        analytics_summary = (
            f"As of Date: {latest_date} | "
            f"Last Closing Price: ${latest_close:.2f} | "
            f"5-Day Simple Moving Average: ${latest_sma:.2f} | "
            f"Automated Signal: {signal}."
        )

        # 4. Extract AI evaluation report
        ai_report = ai_agent.generate_market_report(
            ticker=symbol, analytics_summary=analytics_summary
        )

        # 5. Return a highly structured JSON response to the client web browser
        return {
            "ticker": symbol,
            "date": latest_date,
            "metrics": {
                "close_price": latest_close,
                "moving_average_5d": latest_sma,
                "signal": signal,
            },
            "analysis_report": ai_report,
        }

    except Exception as e:
        # Wrap any internal service exceptions into a clean HTTP 500 error packet
        raise HTTPException(
            status_code=500, detail=f"Pipeline processing failure: {str(e)}"
        )
