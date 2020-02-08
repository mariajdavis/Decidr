import pandas as pd

df = pd.read_csv("dataset//training_data.csv")
ulist = [13, 276, 303]
# for i in range(1, 1600):
#     df2 = df.query(f'user == {i}')
#     if df2.item.size > 100:
#         print(f'{i} : {df2.item.size}')

df2 = df.query(f'user == 276')
l1 = list()
l2 = list()
l3 = list()
l4 = list()
l5 = list()
l6 = list()

count = 0
for i in df2.item:
    if count % 7 == 0:
        l6.append(i)
    elif count % 6 == 0:
        l5.append(i)
    elif count % 5 == 0:
        l4.append(i)
    elif count % 4 == 0:
        l3.append(i)
    elif count % 3 == 0:
        l2.append(i)
    elif count % 2 == 0:
        l1.append(i)

    count -= -1

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)


