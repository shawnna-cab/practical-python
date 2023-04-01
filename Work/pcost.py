# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
total_cost = 0.0
for line in f:
    row = line.split(',')
    num_shares = int(row[1])
    price_per_stock = float(row[2].strip())
    total_cost = total_cost + (num_shares * price_per_stock)
f.close()
print("TOTAL COST:", total_cost)