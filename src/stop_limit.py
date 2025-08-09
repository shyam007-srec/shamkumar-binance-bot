import sys
import logging
import time
from binance_client import MockBinanceClient
from logger import setup_logger
from input_validator import validate_symbol, validate_side, validate_quantity, validate_price


def main():
    setup_logger()
    if len(sys.argv) != 6:
        print("Usage: python stop_limit.py SYMBOL SIDE QUANTITY STOP_PRICE LIMIT_PRICE")
        sys.exit(1)
    _, symbol, side, quantity, stop_price, limit_price = sys.argv

    if not validate_symbol(symbol):
        logging.error(f"Invalid symbol: {symbol}")
        print("Invalid symbol.")
        return
    if not validate_side(side):
        logging.error(f"Invalid side: {side}")
        print("Invalid side.")
        return
    if not validate_quantity(quantity):
        logging.error(f"Invalid quantity: {quantity}")
        print("Invalid quantity.")
        return
    if not validate_price(stop_price) or not validate_price(limit_price):
        logging.error("Invalid price inputs.")
        print("Invalid stop/limit price.")
        return

    client = MockBinanceClient()
    # Simulate price checking loop (in real life, use WebSocket or polling)
    print(f"Waiting for {symbol} price to reach stop price: {stop_price} ...")
    simulated_current_price = float(stop_price) - 50  # Start below stop price
    while simulated_current_price < float(stop_price):
        time.sleep(1)
        simulated_current_price += 10  # Simulate price movement
        print(f"Current price: {simulated_current_price}")
    print("Stop price reached! Placing limit order...")
    order = client.place_limit_order(symbol, side, quantity, limit_price)
    logging.info(f"Placed stop-limit order: {order}")
    print(f"Order result: {order}")

if __name__ == "__main__":
    main()