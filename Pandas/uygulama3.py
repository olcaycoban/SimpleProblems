import pandas as pd

yıllar=[2011,2012,2015,2018]
gelirler=[500,1000,8000,56000]

ülkeler=pd.Series(data=gelirler,index=yıllar)
print(ülkeler)

yıllar=pd.Series(yıllar)
print(yıllar.sum())

print(yıllar.min())
print(yıllar.max())
print(yıllar.product())
print(yıllar.mean())
print(yıllar.median())