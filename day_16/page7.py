from matplotlib import pyplot as plt

companies = ['Google', 'Apple', 'MS', 'Amazon']
revenues = [864, 1068, 1049, 869]
profits = [100, 300, 200, 80]


plt.bar(companies, revenues, label="Revenues")
plt.bar(companies, profits, label="Profits")

plt.xlabel("Companies")
plt.ylabel("Revenues")
plt.title("Tech Companies")

plt.legend()

plt.show()