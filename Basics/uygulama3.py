import numpy as np

dizi1=np.random.randint(1,100,16)
print(dizi1)

dizi1=dizi1.reshape(4,4)
print(dizi1)

for i in dizi1.flat:
    print(i)
for i in np.ndenumerate(dizi1):
    print(i)

a=np.array([2,3,4])
b=np.array([5,6,7])

c=np.hstack([a,b])
print(c)

d=np.vstack([a,b])
print(d)

e=np.array([[1,2],[3,4]])
f=np.array([[5,6]])

g=np.concatenate((e,f),axis=0)
print(g)

h=np.concatenate((e,f.T),axis=1)
print(h)
