import math
# number = 25
# result = math.sqrt(number)
# print(result) 

x = [(1,2), (3,5), (7,8)] # data point axis
y = [0, 0, 1]  # class

# Ucledian distance root of (x2 - x1)^2 + (y2 - y1)^2

# predict data point c = [5,6]
c = [5,6]

# calculating distance UDC function
def UDC(x1, y1):
    x2 = c[0];
    y2 = c[1];
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

dis = [] # distance holding array

for i in range(3):
    distance = UDC(x[i][0], x[i][1])
    #dis.append((round(distance), y[i]))
    dis.append((distance, y[i]))


print(f"distance array for c[5,6] = dis{dis}")
dis.sort() # sorting the 2D list
print(f"after sort = {dis}")


count_0 = 0;
count_1 = 0;

for item in dis:
    if item[1] == 0:
        count_0 = count_0 + 1
    else:
        count_1 = count_1 + 1

print(f"\nTotal zeros = {count_0}\nTotal one = {count_1}")

if(count_0 > count_1):
    print(f"\nIts a class zero")
else:
    print(f"Its a class one")


#-----------------------------------------------------------------#


