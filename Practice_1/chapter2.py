

### python buildin data types

## 1. text type: string

# 1.1 Using single quotes
str1 = 'single quotes'

# 1.2 Using Double quotes
str2 = "Double quotes"

# 1.3 Using Tripple single quotes
str3  = '''Tripple Single quotes'''

# 1.4 Using Tripple Double quotes
str4 = """Tripple Double quotes"""

# 1.5 Four types of printing string
print(f"{1+2}"); print("",1+2)
print(f'{2+3}'); print('',2+3)
print(f"""{3+4}"""); print(""" """,3+4)
print(f'''{4+5}'''); print(''' ''',4+5)

#------------------------------------------------#

## 2. Numeric Types

# 2.1. int
int_type = 12

# 2.2. float type
float_type = 12.10

# 2.3. Complex type
complex_type = 12 + 2j;

#--------------------------------------------------#

## 3. Sequence types

# 3.1. List type (list is an array)
list1 = [1,2,3, 4]

from library import one, two
list2 = [one, two]

array = ['irfan', 'Nusaiba', 'Naira']

for key, value in enumerate(array):
      print(f"key = {key} || value = {value}")

for i in range(2):
  list2[i]()


list3 = [1, 4.5, "string_1", 'string_2', """string_3""", '''string_4''', one, {"name": "Irfan"}, (1,2,3,4, "Irfan"), {1,3,5,8,9}]

for i in range(len(list3)):
        print(f"For i = {i} list3[{i}] = {list3[i]}")


# 3.2. touple type (unique list)

touple1 = (1, 4.5, "string_1", 'string_2', 'string_2' """string_3""", '''string_3''', one, {"name": "Irfan"}, (1,2,3,4, "Irfan"), {1,3,5,8,9})

for i in range(len(touple1)):
        print(f"For i = {i} list3[{i}] = {touple1[i]}")


# 3.3. range type

del list # if there is any list variable on upper then it will be removed from memory
numbers = range(10)
print(list(numbers)) # output is an array [0,1,2,3,4,5,6,7,8,9]
print(list({1, 2, 4})) # output is [1, 2, 4]

my_range = range(10)
# Converting to a list to see values
print(list(my_range))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# x = 10;
# print(f"x = {x}")
# del x; ## del keyword remove variable from memory
# print(f"now x  = {x}")

#-------------------------------------------------------#

# 4. dist type (its a json type object)

dictionary = {"name": "Irfan", "email": "contact@irfans.dev", "portfolioWebsite": "https://irfans.dev"}

print(dictionary)

str = "abcde"

test_arr = ['a', 'b', 'c']

for i in test_arr:
      print(i)

colors = ("red", "green", "blue")
for color in colors:
    print(color)


d_st = {"name": "irfan", "age": "19", "email": "contact@irfans.dev"}
print(d_st.items())

for key, value in enumerate(d_st):
      print(f"key = {key} || value = {value}")

# values in dist
for item in d_st.items():
      print(item)

# keys in dist
for key in d_st.keys():
      print(key)

# values in dist
for value in d_st.values():
      print(value)

# seperate key and value in dist
for key, value in d_st.items():
      print(f"key = {key} || value = {value}")


#-------------------------------------------------------#

# 5. set, frozenset

sets = {'a','b','b','d'}

for key, value in enumerate(sets):
      print(f"key = {key} && value = {value}")



# def check():
#       pass

# print(check())


# for i in range(10):
#       pass


# 