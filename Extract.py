import requests
import pandas as pd

def extract_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data).T
    df.reset_index(inplace=True)
    df.columns = ["crypto_name", "price_usd"]

    return df