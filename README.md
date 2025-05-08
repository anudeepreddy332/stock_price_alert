📖 Description
This Python script monitors Tesla Inc. (TSLA) stock prices using the Alpha Vantage API and sends SMS alerts via Twilio when significant price changes (≥5%) are detected. It also fetches the latest news articles related to Tesla from NewsAPI to provide context for the price movement.

Key Features:
  ✅ Daily stock price tracking (closing price comparison)
  ✅ Percentage change calculation (with 🔺/🔻 indicator)
  ✅ Latest news headlines (top 3 articles)
  ✅ SMS alerts (via Twilio)
  
📂 Repository Structure
stock-price-alerts/  
├── main.py              # Main script (stock tracking + alerts)
├── README.md            # This file  

⚙️ Setup & Usage

1.	Prerequisites
    Python 3.6+
    API keys:
      Alpha Vantage (Stock Data)
      NewsAPI
      Twilio (SMS)

2.	Installation
    git clone https://github.com/yourusername/stock-price-alerts.git
    cd stock-price-alerts

3.	Configuration
    Create config.py and fill in your API keys:
    # config.py
      stock_api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
      news_api_key = "YOUR_NEWSAPI_KEY"
      twilio_account_sid = "YOUR_TWILIO_SID"
      twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"
      my_twilio_no = “Your Twilio phone number”
      receivers_mobile_no = “ Your personal phone number”

4.	Run the Script
    python main.py

5.	Expected Output
    Console logs (stock price difference, news headlines)
    SMS alerts (if price change ≥5%)
    Example SMS:
      TSLA: 🔺5%  
      Headline: Tesla Announces New Battery Breakthrough.  
      Brief: Tesla's latest innovation could reduce costs by 20%...
  	
🛠️ Dependencies
    requests (API calls)
    twilio (SMS notifications)
    Install via:
      pip install requests twilio
      
📜 License
    MIT License - Free for personal and commercial use.

