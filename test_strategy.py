from src.strategy import generate_signal

def test_signal():
    assert generate_signal() in ["BUY", "SELL", "HOLD"]
