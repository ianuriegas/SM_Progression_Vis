import matplotlib.pyplot as plt
import random

balance = 4683.13
x, y = [], []
years_input = int(input("Years : "))
years = 1 + 52 * years_input

for i in range(0, years):
    x.append(i)
    y.append(balance)
    random_float = random.uniform(0.98, 1.05)
    print("Week", str(i) + " ({0:.2f}".format(round(random_float, 2)) + ") : $" + "{0:.2f}".format(round(balance, 2)))
    balance = balance * random_float

plt.plot(x, y)
plt.xlabel('x - Time in weeks')
plt.ylabel('y - Amount in dollars')

plt.title('Randomized tracker graph')
plt.show()
