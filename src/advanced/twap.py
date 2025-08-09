import sys
import logging
import time
from binance_client import MockBinanceClient
from logger import setup_logger
from input_validator import validate_symbol, validate_side, validate_quantity


def main():
    setup_logger()
    if len(sys.argv) != 6:
        print("Usage: python twap.py SYMBOL SIDE TOTAL_QUANTITY NUM_SLICES INTERVAL_SEC")
        sys.exit(1)
    _, symbol, side, total_quantity, num_slices, interval_sec = sys.argv

    if not validate_symbol(symbol):
        logging.error(f"Invalid symbol: {symbol}")
        print("Invalid symbol.")
        return
    if not validate_side(side):
        logging.error(f"Invalid side: {side}")
        print("Invalid side.")
        return
    try:
        total_quantity = float(total_quantity)
        num_slices = int(num_slices)
        interval_sec = int(interval_sec)
        assert total_quantity > 0 and num_slices > 0 and interval_sec > 0
    except Exception:
        logging.error("Invalid TWAP parameters.")
        print("Invalid TWAP parameters.")
        return

    client = MockBinanceClient()
    slice_quantity = total_quantity / num_slices
    for i in range(num_slices):
        order = client.place_market_order(symbol, side, slice_quantity)
        logging.info(f"TWAP slice {i+1}/{num_slices}: {order}")
        print(f"TWAP slice {i+1}/{num_slices}: {order}")
        time.sleep(interval_sec)

    print("TWAP strategy complete.")

if __name__ == "__main__":
    main()