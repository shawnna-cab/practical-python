# report.py
#
# Exercise 2.4
import csv 

# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = row[0], int(row[1]), float(row[2])
#             portfolio.append(holding)
#     return portfolio

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name': row[0], 
                'shares': int(row[1]), 
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = { }
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows: 
            try:
                prices[row[0]] = float(row[1])
            except Exception as error:
                pass
    return prices

portfolio = read_portfolio('./Data/portfolio.csv')
prices = read_prices('./Data/prices.csv')

# total_value = 0.0 
# total_cost = 0.0
# for stock in portfolio:
#     total_value += stock['shares'] * prices[stock['name']]
#     total_cost += stock['shares'] * stock['price']

# print(f'Current value: {total_value:0.2f}')
# print(f'Gain/Loss: {total_cost - total_value:0.2f}')

def make_report(portfolio, prices):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f"{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}")
    print(("-" * 10 + " ") * len(headers))
    report = []
    for stock in portfolio:
        change = float(prices[stock['name']]-stock['price'])
        report.append((stock['name'], stock['shares'], round(prices[stock['name']],2), round(change,2)))
        price = '$' + str(round(prices[stock['name']],2))
        print(f"{stock['name']:>10s} {stock['shares']:>10d} {price:>10s} {change:>10,.2f}")
    return report