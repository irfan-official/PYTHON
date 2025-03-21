 

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'City': ['New York', 'London', 'Paris', 'New York', 'Paris']}
df = pd.DataFrame(data)

encoder = LabelEncoder()
df['City'] = encoder.fit_transform(df['City'])
print(df)

