"""
Request to coingecko https://www.coingecko.com/en/api
the documentation https://www.coingecko.com/en/api/documentation
Our Public API* has a rate limit of 10-30 calls/minute
token_addresses = {
    "levin": "0x1698cD22278ef6E7c0DF45a8dEA72EDbeA9E42aa",
    "weth": "0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1",
    "usdc": "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83"
}

"""

import requests

def get_levin_price():
    try:
        # Token address for Levin on the xDai chain
        levin_address = "0x1698cD22278ef6E7c0DF45a8dEA72EDbeA9E42aa"
        weth_address = "0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1"
        usdc_address = "0xDDAfbb505ad214D7b80b1f830fcCc89B60fb7A83"

        # Coingecko API URL to fetch Levin price in USD
        levin_coingecko_api_url = f"https://api.coingecko.com/api/v3/simple/token_price/xdai?contract_addresses={levin_address}&vs_currencies=usd"
        weth_coingecko_api_url = f"https://api.coingecko.com/api/v3/simple/token_price/xdai?contract_addresses={weth_address}&vs_currencies=usd"
        usdc_coingecko_api_url = f"https://api.coingecko.com/api/v3/simple/token_price/xdai?contract_addresses={usdc_address}&vs_currencies=usd"

        # Fetch the price from Coingecko
        levin_response = requests.get(levin_coingecko_api_url)
        levin_data = levin_response.json()
        weth_response = requests.get(weth_coingecko_api_url)
        weth_data = weth_response.json()
        usdc_response = requests.get(usdc_coingecko_api_url)
        usdc_data = usdc_response.json()

        # Convert levin_address to lowercase
        levin_address_lowercase = levin_address.lower()
        weth_address_lowercase = weth_address.lower()
        usdc_address_lowercase = usdc_address.lower()

        # Get the price of Levin in USD from the response data
        levin_price_usd = levin_data.get(levin_address_lowercase, {}).get("usd", None)
        weth_price_usd = weth_data.get(weth_address_lowercase, {}).get("usd", None)
        usdc_price_usd = usdc_data.get(usdc_address_lowercase, {}).get("usd", None)
        return levin_price_usd,weth_price_usd,usdc_price_usd
    except Exception as e:
        print(f"Error fetching Levin price from Coingecko: {e}")
        return None


# Get the Levin price in USD
list_price_in_usd = get_levin_price()
if list_price_in_usd is not None:
    print("The price of Levin is", list_price_in_usd[0], "USD")
    print("The price of WETH is", list_price_in_usd[1], "USD")
    print("The price of USDC is", list_price_in_usd[2], "USD")
else:
    print("Failed to fetch the Levin price.")
