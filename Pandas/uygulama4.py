import pandas as pd

ülke=pd.read_csv("ülke.csv")
print(ülke)
gelir=pd.read_csv("milligelir.csv")
print(gelir)

print(gelir.head())
print(gelir.head(2))

print(ülke.tail())
print(ülke.tail(2))

toplam=gelir.sum()
print(toplam)