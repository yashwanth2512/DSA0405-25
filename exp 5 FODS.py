import numpy as np

fuel_efficiency = np.array([20, 25, 30, 35, 40])

average = np.mean(fuel_efficiency)

car1 = fuel_efficiency[0]
car2 = fuel_efficiency[4]

improvement = ((car2 - car1) / car1) * 100

print("Fuel efficiency:", fuel_efficiency)
print("Average fuel efficiency:", average, "mpg")
print("Percentage improvement:", improvement, "%")
