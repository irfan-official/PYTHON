<<<<<<< HEAD
import pandas as pd

data = {'Age': [25, 30, 35, 40, 45], 'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)

# Calculating mean and max values
mean_values = df.mean()
max_values = df.max()

print("Mean Values:\n", mean_values)
print("Max Values:\n", max_values)
=======

## import and show a csv file
import pandas as pd
import random 
import numpy as np
## Task - 1 Read CSV file
df = pd.read_csv("pima-indians-diabetes.csv")

## Task - 2 Describe
# print(df.describe())

## Task - 3.1 Tail
# print(df.tail(20))

## Task - 3.2 Head
# print(df.head(20)) 

## Task - 4 Missing value handling
# 1. Dropping rows with missing values
df_cleaned = df.dropna()

## missing value handling with mean vale
mean_df = df.fillna(df.mean())

print(mean_df.head())



## Task - 5.1 drop a clomn
new_drop_column = df.drop(columns=['Number of times pregnant'])

## Task - 5.2 drop a row
new_drop_row = df.drop(index=1)
# print(new_drop_row.head())

## - 5.3 Adding a cloumn
df["New column"] = np.random.randint(1, 100, size=768);
# print(df.head(50))


## - 5.3 Adding a row

# print(df.tail())

new_row = {"Number of times pregnant": 2,
"Plasma glucose concentration a 2 hours in an oral glucose tolerance test": 2, "Diastolic blood pressure (mm Hg)" : 3, "Triceps skin fold thickness (mm)": 4, "2-Hour serum insulin (mu U/ml)" : 5, "Body mass index (weight in kg/(height in m)^2)": 6, "Diabetes pedigree function" : 7, "Age": 8, "Outcome": 10}


df.loc[len(df)] = new_row

# print(df.tail())



# print(df.describe())


## Task - 6.1 Extarct a Row

row = df.iloc[10] # 10 is the row index

print(row)

## Task - 6.2 Extract a column

column = df['Number of times pregnant']

print(column)


>>>>>>> 450eda88aff6576f856a2f052de89ddecdd2e80a
