# Binance Futures Order Bot (Mock Implementation)  

🚀 **A CLI-based trading bot for Binance USDT-M Futures with simulated order execution**  

## 📌 Overview  
The Binance Futures Order Bot (Mock Implementation) is a Python CLI-based trading bot designed for Binance USDT-M Futures.
It was developed as part of an internship assignment to demonstrate trading logic, API interaction, CLI tools, input validation, logging, and modular coding practices — without using a real Binance account or executing live trades.

## ✨ Features  

### 📊 Order Types (Simulated)  
- **Market Orders** – Instant execution at current price  
- **Limit Orders** – Execute only at specified price  
- **Stop-Limit Orders** – Trigger a limit order when stop price is hit  
- **OCO (One Cancels the Other)** – Place two orders; if one executes, the other cancels  
- **TWAP (Time-Weighted Average Price)** – Split large orders into smaller chunks over time  

### 🛠 Core Functionalities  
✔ Mock Binance API Client  
✔ Structured Logging  
✔ Input Validation  
✔ Modular Code  

---

## 📁 Project Structure

```
src/
│
├── market_orders.py # Market order simulation
├── limit_orders.py # Limit order simulation
├── logger.py # Centralized logging utility
├── input_validator.py # Validates user inputs
├── binance_client.py # Mock Binance API
│
├── advanced/
│ ├── stop_limit.py # Stop-Limit order logic
│ ├── oco.py # OCO order simulation
│ └── twap.py # TWAP execution logic
│
├── bot.log # Logs all trades & errors
├── report.pdf # Detailed documentation
└── README.md # Project guide
```

---




## 🖥 How to Run  

### Prerequisites  
- Python 3.8+  
- Clone the repo:  
  ```bash
  git clone https://github.com/shyam007-srec/shamkumar-binance-bot.git
  cd shamkumar-binance-bot/src
### Running Orders
### 1. Market Order
```bash
python market_orders.py BTCUSDT BUY 0.01
```

### 2. Limit Order
```bash
python limit_orders.py BTCUSDT SELL 0.01 41000
```

### 3. Stop-Limit Order
```bash
python advanced/stop_limit.py BTCUSDT BUY 0.01 40500 40600
```

### 4. OCO Order (Take Profit + Stop Loss)
```bash
python advanced/oco.py BTCUSDT SELL 0.01 41500 40500 40400
```

### 5. TWAP Order (Split into chunks)
```bash
python advanced/twap.py BTCUSDT BUY 0.05 5 2
```

---

## 🔑 API Setup

**Mock Mode (Default)**: No API keys needed  
**Live Mode**: Replace `MockBinanceClient` with real API




## 📄 Logging

All actions are logged in `bot.log`, including:
- Timestamps
- Order type
- Symbol, side, quantity, price
- Simulated Order IDs


Example log entries:

```text
2025-08-08 14:25:33 | MARKET BUY | BTCUSDT | Qty: 0.01 | Price: 29250.00
2025-08-08 14:30:12 | LIMIT SELL | ETHUSDT | Qty: 0.1 | Price: 1850.00
```

---

## 🚫 No Real Money Involved

This project uses **simulated trading logic** to mimic the behavior of real Binance Futures orders. No API keys or real funds are used.

---



## Author

Sham Kumar.S  
Junior Python Developer – Crypto Trading Bot

- [Email:](sham1309kumar@gmail.com) sham1309kumar@gmail.com
- [LinkedIn:](https://www.linkedin.com/in/sham-kumar-a10037323) https://www.linkedin.com/in/sham-kumar-a10037323



