# import numpy as np

# arr = np.array([1,2,3])

# print(arr)


# arr2 = np.array([(1,2,3),(4,5,6)])

# print(arr2)

# # Bydefault dtype if float in numpy packasges functions 
# c = np.ones([3,3], dtype=int)

# print(c)


#/////////////////////////////////////////////
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x)

#creating a line plot
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y = sin(x)')
plt.title('simple Line Plot')
plt.show()