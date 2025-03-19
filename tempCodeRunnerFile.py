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
# df_cleaned = df.dropna()
# print(df_cleaned)

## missing value handling with mean vale
mean_df = df.fillna(df.mean())

# print(mean_df.head())



## Task - 5.1 drop a clomn
new_drop_column = df.drop(columns=['Number of times pregnant'])

print(new_drop_column)