import numpy as np

sales = np.array([
    [10, 2, 100],
    [20, 3, 200],
    [15, 4, 300]
])

prices = sales[:, 2]

avg_price = np.mean(prices)

print("Product prices:", prices)
print("Average price:", avg_price)
