
import json
import pandas as pd
from kiteconnect import KiteConnect
from strategy import generate_signal

with open("config.json") as f:
    config = json.load(f)

kite = KiteConnect(api_key=config["api_key"])
kite.set_access_token(config["access_token"])

def fetch_data(instrument_token):
    from datetime import datetime, timedelta
    to_date = datetime.now()
    from_date = to_date - timedelta(minutes=10)
    df = pd.DataFrame(kite.historical_data(
        instrument_token=instrument_token,
        from_date=from_date,
        to_date=to_date,
        interval="minute"
    ))
    return df

def place_order(signal, strike="25100", expiry="25JUL", index="NIFTY"):
    symbol = f"{index}{expiry}{strike}{'CE' if signal == 'BUY_CE' else 'PE'}"
    if config["mode"] == "paper":
        print(f"[PAPER] {signal} -> {symbol}")
        with open("log_trades.csv", "a") as f:
            f.write(f"{signal},{symbol}\n")
    else:
        kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange=kite.EXCHANGE_NFO,
            tradingsymbol=symbol,
            transaction_type=kite.TRANSACTION_TYPE_BUY,
            quantity=config["lot_size"],
            product=kite.PRODUCT_MIS,
            order_type=kite.ORDER_TYPE_MARKET
        )
        print(f"[LIVE] Order placed: {symbol}")

# Example usage (replace with instrument token)
instrument_token = 256265  # NIFTY index token
df = fetch_data(instrument_token)
signal = generate_signal(df)
place_order(signal)
