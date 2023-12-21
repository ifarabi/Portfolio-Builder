import requests
import json

print("Welcome to STONK INFO")
print("Please input the stock ticker of your choice (ALL CAPS)")
tickerChoice = input()
print("Select from the following (Case Sensitive)")
print("Current: Shows current stock price and volume ")
print("Daily: Shows historical day to day stock info ")
print("Weekly: Shows historical stock info on a weekly basis")
print("Monthly: Shows historical stock info on a monthly basis")
print("RSI: Relative Strength Index of stock")

def combine():
    func = input()
    speed = 'error'
    if func == 'Daily':
        speed = 'TIME_SERIES_DAILY'
    elif func == 'Weekly':
        speed = 'TIME_SERIES_WEEKLY'
    elif func == 'Monthly':
        speed = 'TIME_SERIES_MONTHLY'
    elif func == 'Current':
        speed = 'GLOBAL_QUOTE'
    elif func == 'RSI':
        print("How many days of history?")
        days = input()
        print("Would you like to track: low | high | open | close")
        seriesType = input()
        url = 'https://www.alphavantage.co/query?function=' + func + '&symbol=' + tickerChoice + '&apikey=PFIAONBRZUFUKQI3&interval=daily&time_period=' + days + '&series_type=' + seriesType
        return(url)
    else:
        print("Sum Ting Wong")
    url = 'https://www.alphavantage.co/query?function=' + speed + '&symbol=' + tickerChoice + '&apikey=PFIAONBRZUFUKQI3'
    return(url)

#url = 'https://www.alphavantage.co/query?function=' + 'NEWS_SENTIMENT&topics=financial_markets&symbol=TSLA&apikey=PFIAONBRZUFUKQI3'
r = requests.get(combine())
data = r.json()

# with open('results.json', 'w') as convert_file: 
#      convert_file.write(json.dumps(data))
raw = json.loads(json.dumps(data))
formatted = json.dumps(raw, indent=4)
f = open("results.json", 'w')
f.write(formatted)
f.close()
print(formatted)