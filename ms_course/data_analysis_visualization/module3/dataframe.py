import pandas as pd

dataset1 = pd.read_csv("Iris.csv")
dataset1

dataset2 = pd.read_csv("cars.csv")
dataset2.head()
dataset2.info()
dataset2.describe()

# pd.merge()
# pd.concat()
# df.sort_values()
# df.groupby()
# df.agg()
# df.head()