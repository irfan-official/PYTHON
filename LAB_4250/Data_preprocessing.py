# 1. Handling missing dataimport pandas as pd
import numpy as np
import pandas as pd
data = {'Age': [25, np.nan, 30, 35, np.nan], 'Salary': [50000, 60000, np.nan, 80000, 90000]}
df = pd.DataFrame(data)

# Filling missing values with mean
df.fillna(df.mean(), inplace=True)
print(df)

# Dropping rows with missing values
df.dropna(inplace=True)
print(df)

## 2. Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {'City': ['New York', 'London', 'Paris', 'New York', 'Paris']}
df = pd.DataFrame(data)

encoder = LabelEncoder()
df['City'] = encoder.fit_transform(df['City'])
print(df)


## 3. Feature Scaling

from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1, 200], [2, 400], [3, 600]])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data)

## 4. Data Splitting

from sklearn.model_selection import train_test_split
import numpy as np

data = np.arange(1, 11).reshape(-1, 1)
labels = np.arange(1, 11)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
print("Training Data:", X_train)
print("Testing Data:", X_test)


## 5. Statistical Methods

import pandas as pd

data = {'Age': [25, 30, 35, 40, 45], 'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)

# Calculating mean and max values
mean_values = df.mean()
max_values = df.max()

print("Mean Values:\n", mean_values)
print("Max Values:\n", max_values)