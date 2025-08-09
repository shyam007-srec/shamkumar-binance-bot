def validate_symbol(symbol):
    allowed_symbols = ['BTCUSDT', 'ETHUSDT']  # Extend as needed
    return symbol in allowed_symbols

def validate_side(side):
    return side.upper() in ['BUY', 'SELL']

def validate_quantity(quantity):
    try:
        q = float(quantity)
        return q > 0
    except ValueError:
        return False

def validate_price(price):
    try:
        p = float(price)
        return p > 0
    except ValueError:
        return False