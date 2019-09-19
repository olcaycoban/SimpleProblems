import pandas as pd

x=[1,2,3,4,5]

x=pd.Series(x)
print(x)

country=["abd","çin","türkiye","fransa"]
country=pd.Series(country)
print(country)


d=[True,False,True,True]
d=pd.Series(d)
print(d)

gelir={"Türkiye":80000000,
       "Almanya":82000000,
       "Fransa":68000000}
gelir=pd.Series(gelir)
print(gelir)

print(country.values)
print(country.keys())
print(country.dtype)
print(country.shape)
country.name="ülkelerim"
print(country.head())
