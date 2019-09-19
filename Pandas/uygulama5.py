import pandas as pd

ülke=pd.read_csv("ülke.csv",squeeze=True)
print(ülke)
gelir=pd.read_csv("milligelir.csv",squeeze=True)
print(gelir)
print(len(ülke))

print(type(ülke))
print(sorted(gelir))
print(sorted(list(ülke)))
print(dict(gelir))
print(max(gelir))