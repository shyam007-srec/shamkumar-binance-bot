import sys
from binance_client import MockBinanceClient
from logger import setup_logger
from input_validator import validate_symbol, validate_side, validate_quantity, validate_price
import logging

def main():
    setup_logger()
    if len(sys.argv) != 6:
        print("Usage: python limit_orders.py SYMBOL SIDE QUANTITY PRICE")
        sys.exit(1)
    _, symbol, side, quantity, price = sys.argv

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
    if not validate_price(price):
        logging.error(f"Invalid price: {price}")
        print("Invalid price.")
        return

    client = MockBinanceClient()
    order = client.place_limit_order(symbol, side, quantity, price)
    logging.info(f"Placed limit order: {order}")
    print(f"Order result: {order}")

if __name__ == "__main__":
    main()