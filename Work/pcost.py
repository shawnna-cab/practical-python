# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f).split(',')
    total_cost = 0.0
    for line in f:
        row = line.split(',')

        try:
            num_shares = int(row[1])
        except ValueError as error:
            print(error)

        price_per_stock = float(row[2].strip())
        total_cost = total_cost + (num_shares * price_per_stock)
    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)