import numpy as np

house_data = np.array([
    [3, 1200, 200000],
    [5, 1800, 350000],
    [4, 1500, 250000],
    [6, 2200, 450000],
    [5, 2000, 400000]
])

houses = house_data[house_data[:, 0] > 4]

avg_price = np.mean(houses[:, 2])

print("Houses with more than 4 bedrooms:")
print(houses)

print("Average sale price:", avg_price)
