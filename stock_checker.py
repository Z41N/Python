# Importing for date/time and API requesting
import requests
import time
from datetime import datetime

# Set API URL
GPOR_API_URL = 'https://alpha-vantage.p.rapidapi.com/query'

# Set IFTTT webhook+notification applet URL (made @ IFTTT.com)
# NOT USED YET. To be implemented.
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/gpor/with/key/ckjDT2QFfEk7AD1_y6ckTb'

# Function to get GPOR's current price, using RapidAPI
def get_latest_gpor_price():
    querystring = {"symbol": "GPOR", "function": "GLOBAL_QUOTE"}
    headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': "fe6b9725fbmsh571c9148916019cp1b03aejsn7725753b3bfd"
    }
    response = requests.request("GET", GPOR_API_URL, headers=headers, params=querystring)
    response_json = response.json()
    # Printing at that index to output just the price of GPOR
    print("$" + response.text[165:170] + " as of " + str(datetime.now().time().strftime('%I:%M:%S %p')))


print("\nGPOR PRICE:")
# Infinite loop to show the price, with a 5 second delay between pulls
while True:
    get_latest_gpor_price()
    time.sleep(5)
