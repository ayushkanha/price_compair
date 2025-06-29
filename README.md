# 💰 Price Compair Bot

A Python-based bot to compare product prices across multiple e-commerce websites using web scraping. Ideal for budget-conscious shoppers and automation enthusiasts.

## 🔍 Features

- ✅ Scrapes product prices from major online retailers (like Amazon, Flipkart, etc.)
- 📦 Compares and displays the lowest price
- 🔔 Optional: Email or voice alert when prices drop
- 📊 Logs and graphs for historical price tracking (extendable)
- 🌐 Simple interface for entering product names or URLs

## 🧩 Getting Started

### 📋 Prerequisites

- Python 3.8 or higher
- `requests`, `beautifulsoup4`, `lxml` for scraping
- Optional:
  - `smtplib`, `email` for email alerts
  - `pyttsx3` or `gTTS` for voice alerts
  - `matplotlib`, `pandas` for graphing

### 🔧 Installation

```bash
git clone https://github.com/ayushkanha/price_compair.git
cd price_compair
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```
