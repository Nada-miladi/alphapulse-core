from groq import Groq
from src.core.config import settings


class FinancialAgentService:
    def __init__(self):
        # Securely initialize the Groq client engine using our verified configuration
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        # Upgraded to the active Llama 3.1 8B variant supported on Groq
        self.model = "llama-3.1-8b-instant"

    def generate_market_report(self, ticker: str, analytics_summary: str) -> str:
        """
        Submits structured financial calculations to Llama-3.1 via Groq
        and extracts an advanced executive summary.
        """
        system_prompt = (
            "You are an elite Wall Street Quantitative Analyst and Executive Advisor. "
            "Your task is to review technical indicators, filter out market noise, and "
            "provide extremely concise, sharp, and data-driven market commentary. "
            "Do not use generic filler words. Speak with absolute precision and professional gravity."
        )

        user_prompt = f"Analyze the following data matrix for asset ticker: {ticker}.\nData Summary:\n{analytics_summary}"

        # Dispatch the request to Groq's high-speed LPU infrastructure
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,  # Lower temperature forces deterministic, highly structured analysis
        )

        return completion.choices[0].message.content
