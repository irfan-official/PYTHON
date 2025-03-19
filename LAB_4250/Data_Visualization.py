
### Types of Data Visualization Methods

## 1. Line Plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='Sine Wave')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Line Plot Example')
plt.legend()
plt.show()

## 2. Bar Chart
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()


## 3. Histogram

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()

## 4. Scatter Plot

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter Plot Example')
plt.show()

# 5. Pie Chart

import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 25, 25]
colors = ['gold', 'lightblue', 'lightcoral', 'lightgreen']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart Example')
plt.show()

## 6. Box Plot
import numpy as np
import matplotlib.pyplot as plt

data = [np.random.randn(100) for _ in range(4)]
plt.boxplot(data, patch_artist=True)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot Example')
plt.show()

## Bangladesh vs china in population growth

import matplotlib.pyplot as plt

# Corrected country name spelling and variable names
data_bd = {
    "Country": ["Bangladesh"] * 10,
    "Year": [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990],
    "Population": [2000000, 3500000, 4500000, 6000000, 7000000, 8000000, 9000000, 11000000, 12000000, 13500000]
}

data_china = {  # Fixed "Chaina" to "China"
    "Country": ["China"] * 10,
    "Year": [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990],
    "Population": [4000000, 5500000, 6500000, 7000000, 8000000, 9000000, 10000000, 12000000, 13000000, 14000000]
}

x = data_bd["Year"]
y = data_china["Year"]

plt.plot(x, data_bd["Population"], label="Bangladesh", color="red", linestyle='--')
plt.plot(y, data_china["Population"], label="China", color="blue", linestyle='-') 
# Labels and title
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth of Bangladesh and China")
plt.legend()

# Show plot
plt.show()