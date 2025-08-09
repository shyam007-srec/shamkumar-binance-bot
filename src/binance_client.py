import logging

class MockBinanceClient:
    def __init__(self):
        logging.info("Initialized mock Binance client.")

    def place_market_order(self, symbol, side, quantity):
        # Simulate API response
        return {
            "status": "FILLED",
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "price": "40000.00"  # Example price
        }

    def place_limit_order(self, symbol, side, quantity, price):
        return {
            "status": "NEW",
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "quantity": quantity,
            "price": price
        }

    # Add mock methods for stop-limit, OCO, TWAP, etc.