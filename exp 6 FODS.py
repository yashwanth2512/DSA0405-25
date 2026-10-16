prices = [100, 200, 300]
quantities = [2, 1, 3]

discount_rate = 10
tax_rate = 5

total = 0

for i in range(len(prices)):
    total += prices[i] * quantities[i]

discount = total * discount_rate / 100
after_discount = total - discount

tax = after_discount * tax_rate / 100
final_cost = after_discount + tax

print("Original cost:", total)
print("Discount:", discount)
print("Cost after discount:", after_discount)
print("Tax:", tax)
print("Final cost:", final_cost)
