
import pandas as pd
from ta.momentum import RSIIndicator

def calculate_vwap(df):
    return (df['volume'] * (df['high'] + df['low'] + df['close']) / 3).cumsum() / df['volume'].cumsum()

def generate_signal(df):
    df['rsi'] = RSIIndicator(df['close'], window=7).rsi()
    df['vwap'] = calculate_vwap(df)

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    if latest['close'] > latest['vwap'] and latest['rsi'] > 60 and latest['close'] > prev['high']:
        return "BUY_CE"
    elif latest['close'] < latest['vwap'] and latest['rsi'] < 40 and latest['close'] < prev['low']:
        return "BUY_PE"
    else:
        return "WAIT"
