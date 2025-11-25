import numpy as np
import pandas as pd

class MetricsEngine:
    def __init__(self, df):
        self.df = df.copy()

    def correlation(self, col1, col2):
        return self.df[col1].corr(self.df[col2])

    def rolling_mean_sentiment(self, window=7):
        self.df["Sentiment_Rolling"] = self.df["sentiment"].rolling(window).mean()
        return self.df

    def daily_returns(self):
        self.df["Returns"] = self.df["Close"].pct_change()
        return self.df

    def sentiment_price_relation(self):
        return self.df[["sentiment", "Close"]].corr().iloc[0, 1]
