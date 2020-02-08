import pandas as pd

df = pd.read_csv("dataset//training_data.csv")
ulist = [13, 276, 303]
# for i in range(1, 1600):
#     df2 = df.query(f'user == {i}')
#     if df2.item.size > 100:
#         print(f'{i} : {df2.item.size}')

df2 = df.query(f'user == 13')
print(df2)
# print(f'{df2.item.size}')

