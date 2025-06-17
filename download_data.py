
import requests
from datetime import datetime

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202506"
response = requests.get(url)

if response.status_code == 200:
    filename = f"treasury_yield_curve_{datetime.now().strftime('%Y-%m-%d')}.html"
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Saved as {filename}")
else:
    print("Failed to download data")
