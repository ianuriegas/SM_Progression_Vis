import matplotlib.pyplot as plt

balance = 4683.11

# total_years = int(input("Input the amount of years we want to track: "))
# years_to_weeks = 1 + 52 * total_years
total_weeks = int(input("Enter Weeks: "))

count_year = 1
percentages = [1.01, 1.02, 1.03, 1.04, 1.05]
x, y, graph_points = [], [], []

for j in range(0, 5):
    for i in range(0, total_weeks):
        x.append(i)
        y.append(balance)
        if i == 1 or (i - 1) % 52 == 0:
            print("\nYEAR: " + str(count_year))
            count_year = count_year + 1

        # print("Week", str(i) + ": $" + "{0:.2f}".format(round(balance, 2)))
        balance = balance * percentages[j]
    graph_points.append(x)
    graph_points.append(y)
    x, y = [], []
    balance = 4683.11
    count_year = 1

j = 0
for i in range(0, 10):
    if i % 2 == 1:
        plt.plot(graph_points[i - 1], graph_points[i], label=percentages[j])
        # plt.scatter(graph_points[i - 1], graph_points[i], label="stars", color="green", marker="*", s=30)
        j = j + 1

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Stock growth')
plt.legend()
plt.show()
