import pandas as pd
from src.metrics import MetricsEngine

def test_correlation():
    df = pd.DataFrame({
        "sentiment": [1, 2, 3, 4],
        "Close":     [10, 11, 12, 13]
    })
    m = MetricsEngine(df)
    value = m.correlation("sentiment", "Close")
    assert value > 0
