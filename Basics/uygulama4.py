import numpy as np

a=np.array([10,20,30,40])
b=np.arange(4)
c=a+b
print(c)
c=c**2
print(c)
c+=10
print(c)
x=np.random.random(9)
print(x)
print(x.max())
print(x.min())
print(x.sum())

dizi1=np.arange(15).reshape(3,5)
print(dizi1)
print(dizi1.sum(axis=0))
print(dizi1.sum(axis=1))
print(dizi1.max(axis=1))
print(dizi1.cumsum(axis=1))


