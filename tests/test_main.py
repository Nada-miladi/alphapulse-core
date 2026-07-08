import pytest
from src.main import run_alpha_pulse_analysis


def test_system_orchestration_pipeline_execution(capsys):
    """Verify that the central orchestration logic coordinates components without crashing."""
    run_alpha_pulse_analysis("MSFT")

    # Capture everything printed out to the terminal screen
    captured = capsys.readouterr()

    # Assertions to ensure professional terminal prints match our expectations
    assert "Initializing AlphaPulse Core Analysis Engine" in captured.out
    assert "ALPHAPULSE EXECUTIVE MARKET INTELLIGENCE REPORT" in captured.out
    assert "Critical Pipeline Failure" not in captured.err
