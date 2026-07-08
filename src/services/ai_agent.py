from groq import Groq
from src.core.config import settings


class FinancialAgentService:
    def __init__(self):
        # Securely initialize the Groq client engine
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = "llama-3.1-8b-instant"

    def _execute_agent_inference(self, system_prompt: str, user_prompt: str) -> str:
        """Helper method to isolate Groq inference requests cleanly."""
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
        )
        return completion.choices[0].message.content

    def generate_market_report(self, ticker: str, analytics_summary: str) -> str:
        """
        Orchestrates a multi-agent team consensus loop:
        1. Technical Analyst evaluates raw statistical math indicators.
        2. Macro Economist evaluates high-level market context.
        3. Portfolio Manager synthesizes both outputs into a definitive action plan.
        """

        # Agent 1: The Technical Specialist
        tech_analyst_system = (
            "You are an elite Wall Street Technical Analyst specializing in momentum and price action. "
            "Analyze the provided metrics strictly through the lens of math, support/resistance, "
            "and moving average deviations. Provide a highly precise technical brief."
        )
        tech_analyst_user = f"Evaluate these quantitative calculations for asset {ticker}:\n{analytics_summary}"
        tech_brief = self._execute_agent_inference(
            tech_analyst_system, tech_analyst_user
        )

        # Agent 2: The Macro Economist
        macro_economist_system = (
            "You are a global Macro Economist and Fed Policy Specialist. "
            "Evaluate current institutional market dynamics, sector momentum shifts, inflation-interest rate pressures, "
            "and structural economic risks. Keep your commentary highly professional and macro-focused."
        )
        macro_economist_user = f"Provide a brief macro risk overlay context for trading the {ticker} asset ticker right now."
        macro_brief = self._execute_agent_inference(
            macro_economist_system, macro_economist_user
        )

        # Agent 3: The Lead Portfolio Manager (The Synthesizer)
        portfolio_mgr_system = (
            "You are an institutional Portfolio Manager and Chief Investment Officer. "
            "Your job is to read separate briefs from your Technical Analyst and Macro Economist, "
            "resolve any conflicting perspectives, filter out the noise, and issue a final, "
            "ultra-polished, executive asset allocation report. Speak with absolute authority and absolute precision."
        )
        portfolio_mgr_user = (
            f"Asset Under Review: {ticker}\n\n"
            f"--- Technical Analyst Brief ---\n{tech_brief}\n\n"
            f"--- Macro Economist Brief ---\n{macro_brief}\n\n"
            "Synthesize these expert insights and compile the ultimate AlphaPulse Executive Report."
        )

        final_report = self._execute_agent_inference(
            portfolio_mgr_system, portfolio_mgr_user
        )
        return final_report
