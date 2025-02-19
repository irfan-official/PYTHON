import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
names = ["Irfan", "Naira", "Nusaiba", "Kakasha", "Alice", "Bob", "Tramp"]

arr = []

for i in range(100):
  arr.append({"name":random.choice(names), "score": random.randint(40, 100)})



df = pd.DataFrame(arr)


# print(df)

# plt.figure(figsize=(10, 6))
# plt.bar(range(len(df)), df['score'], color='skyblue')
# plt.xticks(range(len(df)), df['name'])
# plt.xlabel('Name')
# plt.ylabel('Score')
# plt.title('Scores by Name')
# for i, v in enumerate(df['score']):
#     plt.text(i, v + 2, str(v), ha='center')
# plt.show()



plt.figure(figsize=(10, 6))
sns.barplot(x="name", y="score", data=df, palette="viridis", ci=None)

plt.title("Scores of Randomly Chosen Names")
plt.xlabel("Name")
plt.ylabel("Score")
plt.show()