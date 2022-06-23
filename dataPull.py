import requests
import json
import pandas as pd

# def dataPull():
#     r = requests.get('https://api.cryptowat.ch/markets/kraken/btcusd/ohlc')
#     print(r.json())
#     with open('temp.json','w') as f:
#         json.dump(r.json(), f)
#     pandasData = pd.read_json(r.json())
#     return (pd.read_json(r.json()))

# r = requests.get('https://api.cryptowat.ch/markets/kraken/btcusd/ohlc')
# print(r.json())
# with open('temp.json','w') as f:
#     json.dump(r.json(), f)



# load data using Python JSON module
# with open('temp.json','r') as f:
#     data = json.loads(f.read())
# # Flatten data
# df_nested_list = pd.json_normalize(data, record_path =['result'])
# df_nested_list.info()


# load data using Python JSON module
# with open('temp.json','r') as f:
#     data = json.loads(f.read())

# # Normalizing data
# df = pd.json_normalize(
#     data, 
#     record_path =['result'],
#     meta=[
#         'timeframe'
#     ])
# df.info()

#newTempData = pd.concat([pd.DataFrame(json_normalize(x)) for x in tempData['json']],ignore_index=True)
#newTempData = pd.concat([pd.DataFrame(json_normalize(x)) for x in tempData['result'][0]],ignore_index=True)

# tempData = pd.read_json('temp.json')
# tempData.info()

df = pd.read_json("temp.json", lines=True)
df.info()
# df['result'][0]


# load data using Python JSON module
with open('temp.json','r') as f:
    data = json.loads(f.read())
data
# Flatten data
df_nested_list = pd.json_normalize(data, record_path =['result'])
df_nested_list

# returns subset of data
# for x in tempData['result'][0]:
#     print(x)


# def dataPull():
#     df = pd.read_json("temp.json", lines=True)
#     df_nested_list = pd.json_normalize(df, record_path =['result'][0])
#     df_nested_list.info()

#     return df_nested_list

# dataPull()