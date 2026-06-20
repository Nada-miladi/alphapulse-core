from src.core.config import settings


def test_settings_load_successfully():
    """Verify that configuration attributes parse successfully from the environment file."""
    assert settings.APP_NAME == "AlphaPulse Core"
    assert settings.ENVIRONMENT == "development"
    assert settings.GROQ_API_KEY is not None
    assert len(settings.GROQ_API_KEY) > 0
