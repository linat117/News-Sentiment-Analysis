import pandas as pd
from src.indicators import IndicatorEngine

def test_rsi():
    df = pd.DataFrame({"Close": [10, 11, 12, 11, 10, 9, 8, 12, 14, 15]})
    engine = IndicatorEngine(df)
    result = engine.add_rsi()
    assert "RSI" in result.columns
