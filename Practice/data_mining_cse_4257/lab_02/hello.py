
#Introduction to Data Mining with NumPy, Pandas and Mathplotlib

import numpy as np


# arr2 = np.array([1,2,3])
# print(f"arr2 = {arr2}")

# arr = [[1,2,3],[4,5,6],[7,8,9]];


# for i in arr:
#     print(i)

a = np.array([1,2,3])


# b = np.array([(1,2,3),(4,5,6)], dtype=float)
# c= np.ones([1,3])
# g = c-b
# print(g)

# srt = np.sort(a)
# print(srt)
# print(a,b)

# zero = np.zeros([3,3])
# zero2 = np.zeros((3,3))
# zero3 = np.ones((3,3, 2))
# print(zero3)



# ones = np.ones((2,3,4), dtype=np.int16)

# print(ones)


# num = np.arange(100,200)

# print(f"number = {num}")


# num2 = np.linspace(0,100,10)

# print(f"number = {num2}")

num3 = np.full((2,2),7)

# print(num3)

# identity_matrices = np.eye(3)


# import random

# # num4 = random.random()
# # num5 = np.random.random(2,2)
# # print(f"random number = {num5}"
# arr1d = [1,2,3,4,5]
# arr_sum = np.sum(arr1d)
# arr_sum = np.mean(arr1d)
# arr_min_elem = np.min(arr1d)
# arr_max_elem = np.max(arr1d)

# print(arr_max_elem)

# arr = "array([1,2,3])"
# print(arr)

# arr2 = "array([[1., 2., 3],[4., 5., 6.]])"
# print(arr2) 

# arrr = [1,2,3,4,5,6]

# print(arrr[:4])

from random import random as rn, randint as rd

# Problem no 01

# l_s = 0
# l_e = 100
# arr3 = [[rd(l_s,l_e),rd(l_s,l_e),rd(l_s,l_e)],
#         [rd(l_s,l_e),rd(l_s,l_e),rd(l_s,l_e)],
#         [rd(l_s,l_e),rd(l_s,l_e),rd(l_s,l_e)]]

# sum = 0
# for i in arr3:
#     sum += np.sum(i)

# print(f"sum of array = {sum}")

# # Problem no 02

# arr1 = np.array([12,52,33])
# arr2 = np.array([43,52, 66])

# mul_arr = arr1 * arr2

# print(f"multiplication of array = {mul_arr}")




import pandas as pd

data = {"Name": ['Alice','charlie', 'David','Eva'], "Age": [25, 30,22,28], "Salary": [50000, 60000, 45000, 70000]}

df = pd.DataFrame(data)
print(df)
print("///////////////////////////")
row_0 = df.iloc[0]
print(row_0)

let_one_age = df.iloc[1, df.columns.get_loc('Age')]
print(let_one_age)

select_rows = df.loc[[1,3]]
print("///////////////////////////")

print(select_rows)

print("//////////////////////////")

cell_label = df.loc[2, 'Salary']
print(cell_label)


print("/////////////////////////")

salary = df[df['Salary'] > 55000]
print(salary)
print("/////////////////////////")
#Setting value in data frame

print(df.loc[0, "Age"])
df.loc[0, "Age"] = 26
print(df.loc[0, "Age"])
print("////////////////////////")
#settinf a new columns

df["Experience"] = [2,5,1,7]

print(df)