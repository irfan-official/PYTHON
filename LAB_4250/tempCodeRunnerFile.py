import pandas as pd

data = {'Age': [25, 30, 35, 40, 45], 'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)

# Calculating mean and max values
mean_values = df.mean()
max_values = df.max()

print("Mean Values:\n", mean_values)
print("Max Values:\n", max_values)