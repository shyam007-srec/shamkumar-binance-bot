import sys
from binance_client import MockBinanceClient
from logger import setup_logger
from input_validator import validate_symbol, validate_side, validate_quantity
import logging

def main():
    setup_logger()
    if len(sys.argv) != 5:
        print("Usage: python market_orders.py SYMBOL SIDE QUANTITY")
        sys.exit(1)
    _, symbol, side, quantity = sys.argv

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

    client = MockBinanceClient()
    order = client.place_market_order(symbol, side, quantity)
    logging.info(f"Placed market order: {order}")
    print(f"Order result: {order}")

if __name__ == "__main__":
    main()