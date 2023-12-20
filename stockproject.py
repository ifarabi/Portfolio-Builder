import requests
import json

# print("Select from the following: ")
# input1 = input()
url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=financial_markets&symbol=TSLA&apikey=PFIAONBRZUFUKQI3'
r = requests.get(url)
data = r.json()

with open('results.json', 'w') as convert_file: 
     convert_file.write(json.dumps(data))
print("Done!")