
import numpy as np
import matplotlib.pyplot as plt

# x = np.linespace(0, 10, 100);
# y = np.sin(x)
# plt.plot(x,y, label="Sine Wave", color="red", linestyle='--')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title("Data Visulization")
# plt.legend()
# plt.show()

## ...............................................

# x = np.linspace(0, 10, 100)  # Fixed np.linespace -> np.linspace

# # Compute sine and cosine values
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# # Plot sine wave
# plt.plot(x, y_sin, label="Sine Wave", color="red", linestyle='--')

# # Plot cosine wave
# plt.plot(x, y_cos, label="Cosine Wave", color="blue", linestyle='-')

# # Labels and title
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title("Sine and Cosine Waves")

# # Show legend
# plt.legend(loc="upper right")

# # Display the plot
# plt.show()

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

# Show plot
plt.show()


import matplotlib.pyplot as plt
data_Irfan = {
    "skill": ["javaScript", "python", "github", "c++"],
    "semister": ["1st", "2nd", "3rd", "4th"],
}
data_mahin = {
    "skill": ["javaScript", "python","", "c++"],
    "semister": ["1st", "2nd", "3rd", "4th"],
}

plt.plot( data_Irfan["semister"], data_Irfan["skill"], label="Irfan the Boss", color="red", linestyle="-")
plt.plot(data_mahin["semister"],data_mahin["skill"],  label="Mahin the mao", color="blue", linestyle="--")

plt.legend()
plt.xlabel("semister")
plt.ylabel("skill")
plt.title("Growth of mentality")
plt.show()