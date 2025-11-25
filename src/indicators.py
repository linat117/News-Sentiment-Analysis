import talib
import pandas as pd

class IndicatorEngine:
    def __init__(self, df):
        self.df = df.copy()

    def add_rsi(self, period=14):
        self.df["RSI"] = talib.RSI(self.df["Close"], timeperiod=period)
        return self.df

    def add_sma(self, period=20):
        self.df[f"SMA_{period}"] = talib.SMA(self.df["Close"], timeperiod=period)
        return self.df

    def add_ema(self, period=20):
        self.df[f"EMA_{period}"] = talib.EMA(self.df["Close"], timeperiod=period)
        return self.df

    def add_macd(self):
        macd, signal, hist = talib.MACD(self.df["Close"])
        self.df["MACD"] = macd
        self.df["MACD_Signal"] = signal
        self.df["MACD_Hist"] = hist
        return self.df
