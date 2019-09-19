import pandas as pd

ülke=pd.read_csv("ülke.csv",squeeze=True)
gelir=pd.read_csv("milligelir.csv",squeeze=True)

print(ülke)
print(ülke[15::-3])
print(ülke[0:16:3])

print(len(gelir))
print(gelir.count())
print(gelir.sum())
print(gelir.mean())
print(gelir.median())
print("----------------------")
print(gelir.describe())