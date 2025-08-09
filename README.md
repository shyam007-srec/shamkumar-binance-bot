# Binance Futures Order Bot (Mock Implementation)

## Overview
This is a CLI-based trading bot for Binance USDT-M Futures, implemented for assignment and demonstration purposes. As I am under 18 and unable to register on Binance, this bot uses a mock API client to simulate order placement and management.

## Features
- Place Market and Limit orders via CLI
- Simulate advanced order types: Stop-Limit, OCO, TWAP
- Structured logging to `bot.log`
- Input validation and error handling
- Modular codebase for easy extension

## How to Run

1. Install Python 3.x
2. Clone this repository and navigate to the `/src` folder
3. Run orders:
   - **Market Order:**  
     `python market_orders.py BTCUSDT BUY 0.01`
   - **Limit Order:**  
     `python limit_orders.py BTCUSDT SELL 0.01 41000`
   - **Stop-Limit Order:**  
     `python advanced/stop_limit.py BTCUSDT BUY 0.01 40500 40600`
   - **OCO Order:**  
     `python advanced/oco.py BTCUSDT SELL 0.01 41500 40500 40400`
   - **TWAP Order:**  
     `python advanced/twap.py BTCUSDT BUY 0.05 5 2`

## API Setup
No API keys required for mock mode. To switch to real API, replace `MockBinanceClient` with the actual Binance client and provide API credentials.

## File Structure
```
src/
  market_orders.py
  limit_orders.py
  logger.py
  input_validator.py
  binance_client.py
  advanced/
    stop_limit.py
    oco.py
    twap.py
bot.log
report.pdf
README.md
```

## Logging
All actions, errors, and order executions are logged in `bot.log` with timestamps.

## Documentation & Report
See `report.pdf` for screenshots and implementation analysis.

## Contact for Submission
Send your resume and completed assignment, along with the log files, to:
- saami@bajarangs.com
- nagasai@bajarangs.com
- chetan@bajarangs.com
- CC: sonika@primetrade.ai

Subject: "Junior Python Developer – Crypto Trading Bot"
