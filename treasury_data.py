# getting treasury yields 

#import yfinance
import yfinance as yf 

tickers = {
        "13 weeks": "^IRX",
        "2 years futures: "ZT=F",
        "3 years futures: "ZN3=F", 
        "5 years": "^FVX",
        "10 years": "^TNX",
        "30 years": "^TYX"
}

def calculate_bond_yield(futures_price, coupon_rate=0.06, years=10, face_value=100):
    """
    Calculate approximate yield from Treasury futures price using bond math.
    Args:
        futures_price: Current ZN=F futures price
        coupon_rate: Annual coupon rate (6% is standard for 10Y Treasuries)
        years: Time to maturity
        face_value: Principal amount
    Returns:
        Implied yield in percentage
    """
    cash_flows = np.full(years, coupon_rate * face_value)
    cash_flows[-1] += face_value  # Add principal at maturity
    return npf.irr([-futures_price] + list(cash_flows)) * 100
        

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
                # Special handling for bond futures
                if name == "US-10 Year Bond Futures":
                    yield_value = calculate_bond_yield(last_close)
                    data.append([name, f"{last_close:.2f}", f"{change:.2f}", f"{percent_change:.2f}%"])
                    data.append(["US-10Y Implied Futures Yield", f"{yield_value:.2f}%", f"{change:.2f}", f"{percent_change:.2f}%"])

            else:
                data.append([name, "No Data", "N/A", "N/A"])

        except Exception as e:
            print(f"Error fetching {name}: {str(e)}")
            data.append([name, "Error", "Error", "Error"])
print(data)



  

get_market_data()

