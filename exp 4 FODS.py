import numpy as np

sales_data = np.array([10000, 15000, 18000, 25000])

total_sales = np.sum(sales_data)

increase = ((sales_data[3] - sales_data[0]) /
            sales_data[0]) * 100

print("Quarterly sales:", sales_data)
print("Total annual sales:", total_sales)
print("Percentage increase:", increase, "%")
