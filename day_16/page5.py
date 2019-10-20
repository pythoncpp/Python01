from matplotlib import pyplot as plt

print(plt.style.available)

# plt.xkcd()

plt.style.use('bmh')

ages = [20, 23, 25, 26, 30, 32, 35, 37, 39, 40]
salaries = [30000, 35000, 37000, 40000, 30000, 45000, 50000, 60000, 70000, 80000]
expenses = [1000, 4000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 55000]

# create a line chart
plt.plot(ages, salaries, label="Salaries")
plt.plot(ages, expenses, label="Expenses", color="red")

# set the titles
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.title("Age Vs Salary")

# legend
plt.legend()

# save the graph
plt.savefig('age_vs_salary.png')

plt.show()
