import sys
import logging
from binance_client import MockBinanceClient
from logger import setup_logger
from input_validator import validate_symbol, validate_side, validate_quantity, validate_price


def main():
    setup_logger()
    if len(sys.argv) != 7:
        print("Usage: python oco.py SYMBOL SIDE QUANTITY PRICE STOP_PRICE STOP_LIMIT_PRICE")
        sys.exit(1)
    _, symbol, side, quantity, price, stop_price, stop_limit_price = sys.argv

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
    if not all(map(validate_price, [price, stop_price, stop_limit_price])):
        logging.error("Invalid price inputs.")
        print("Invalid price(s).")
        return

    client = MockBinanceClient()
    # Simulate OCO: Place take-profit and stop-limit, cancel one when the other is filled
    tp_order = client.place_limit_order(symbol, side, quantity, price)
    sl_order = client.place_limit_order(symbol, side, quantity, stop_limit_price)
    logging.info(f"OCO order placed: Take Profit {tp_order}, Stop Limit {sl_order}")
    print(f"OCO Orders placed:\nTake Profit: {tp_order}\nStop Limit: {sl_order}")

    # Simulate one order getting filled
    import random
    filled = random.choice(['TP', 'SL'])
    if filled == 'TP':
        logging.info("Take Profit filled, cancelling Stop Limit.")
        print("Take Profit order filled! Stop Limit order cancelled.")
    else:
        logging.info("Stop Limit filled, cancelling Take Profit.")
        print("Stop Limit order filled! Take Profit order cancelled.")

if __name__ == "__main__":
    main()