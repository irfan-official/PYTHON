import pandas as pd
import numpy as np
import random

database_1 = {
    "name": ["Irfan", "Rohan", "Naira"],
    "age" : [23, 18, 6],
    "gender": ["M", "M", "F"],
    "score" : [97, 45, 90]
}

names = ["Ayaan", "Zoya", "Kabir", "Meera", "Rahul", "Ananya", "Aryan", "Saanvi", "Vikram", "Pooja", f"{np.nan}"]
genders = ["M", "F",  f"{np.nan}"]
# random_Age = random.randint(5,60)
age = [random.randint(5,60), np.nan]
score = [random.randint(0, 100), np.nan]

for _ in range(1000):
    database_1["name"].append(random.choice(names))
    database_1["age"].append(random.choice(age))  # Random age between 5 and 60
    database_1["gender"].append(random.choice(genders))
    database_1["score"].append(random.choice(score))  # Random score between 30 and 100

df1 = pd.DataFrame(database_1)

# df1.to_csv("sample_of_1000.csv")

# print(df1.head(60)) ## Print the total 60 rows from start

# print(df1.dropna()) ## Drop the NaN contains rows

# new_dist = df1.fillna(0)
# print(df1.head(60))

# df1.tail(5) // output value from last


## 
# df2 = df1.fillna(0) # return dist 
# df3 = df2["score"].fillna(df2["score"].mean()) ## modify dist ## fill value by mean
# print(df2.head(40)) 

# df2.to_csv("df2.csv")

df_filled_mean = df1.fillna(df1.mean(numeric_only=True))

print(df_filled_mean.head(30))

# Print the mean of numeric color
# print(df1.mean(numeric_only=True))