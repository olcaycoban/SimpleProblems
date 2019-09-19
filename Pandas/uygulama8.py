import pandas as pd

kıta=pd.read_csv("kıta.csv",squeeze=True)
gelir=pd.read_csv("milligelir.csv",squeeze=True)

print(kıta)

print(kıta.value_counts())
print(kıta.value_counts(ascending=True))

min=gelir.idxmin()
print(min)
min=gelir[min]
print(min)

max=gelir.idxmax()
print(max)
max=gelir[max]
print(max)

def func(gel):
    if gel<2000000:
        return ("Orta")
    elif gel>=2000000 and gel<5000000:
        return ("Yüksek")
    else:
        return ("Çok Yüksek")

print(gelir.apply(func))

print(gelir.apply(lambda l:l*2))