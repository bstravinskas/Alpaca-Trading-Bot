from contextlib import redirect_stdout
import config, requests, json

holdings = open('data/qqq.csv').readlines()

# for holding in holdings:
#     print(holding)

symbols = [holding.split(',')[2].strip() for holding in holdings][1:]
symbols = ",".join(symbols)
print(symbols)

# minute_bars_url = config.BARS_URL + '/5Min?symbols=MSFT&limit=1000'
day_bars_url = '{}/day?symbols={}&limit=1000'.format(config.BARS_URL, symbols)

r = requests.get(day_bars_url, headers=config.HEADERS)

print(json.dumps(r.json(), indent=4))


with open('output.txt', 'w') as f:
    with redirect_stdout(f):
        print(json.dumps(r.json(), indent=4))
