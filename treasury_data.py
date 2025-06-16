# getting treasury yields 

#import yfinance
import yfinance as yf 

tickers = {
        "13 weeks": "^IRX",
        "5 years": "^FVX",
        "10 years": "^TNX",
        "30 years": "^TYX"
}


#function to get current yield rates
def get_market_data(): 
    """Fetch market data with enhanced error handling"""
    data = []
    
    # Get other market data
    for name, symbol in tickers.items():
        try:
            asset = yf.Ticker(symbol)
            info = asset.history(period="2d")
            
            if not info.empty and len(info) >= 2:
                last_close = info["Close"].iloc[-1]
                prev_close = info["Close"].iloc[-2]
                change = last_close - prev_close
                percent_change = (change / prev_close) * 100
                
                # Format numbers based on asset type      
                if any(x in name for x in ["weeks", "years"]):
                    data.append([name, f"{last_close:,.2f}"])

            else:
                data.append([name, "No Data", "N/A", "N/A"])

        except Exception as e:
            print(f"Error fetching {name}: {str(e)}")
            data.append([name, "Error", "Error", "Error"])


get_market_data()
