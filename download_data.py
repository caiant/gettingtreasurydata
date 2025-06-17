from datetime import datetime
import csv
import requests
import re



url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202506"
response = requests.get(url)
decoded_content = response.content.decode('utf-8')
if response.status_code == 200:
    filename = f"treasury_yield_curve_{safe_date_str}.html"
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Saved as {filename}")
else:
    print("Failed to download data")
