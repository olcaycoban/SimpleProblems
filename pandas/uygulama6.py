import pandas as pd

ülke=pd.read_csv("ülke.csv",squeeze=True)
gelir=pd.read_csv("milligelir.csv",squeeze=True)

print(ülke.sort_values().head(5-2))
print(gelir.sort_values(ascending=False))
print(gelir.sort_values(ascending=False).tail(2))
print(gelir.sort_values(ascending=True))

print("ABD" in ülke.values)