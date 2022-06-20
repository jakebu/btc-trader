import requests
import json
r = requests.get('https://api.cryptowat.ch/markets/kraken/btcusd/ohlc')
r.json()
print(r.json())
with open('temp.json','w') as f:
    json.dump(r.json(), f)