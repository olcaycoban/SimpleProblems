import pandas as pd

x=[1,2,3,4,5]
print(x)
ser = pd.Series(x)
print(ser)

ülke=["Abd","Çin","Türkiye","Fransa"]
ülke1=pd.Series(ülke)
print(ülke1)
print(ülke1.index)
ülke1.name="Ülkeler"
print(ülke1)

b=[True,False,False]
b1=pd.Series(b)
print(b1)