import numpy as np

dizi1=np.array([1,2,3,4,5])
print(dizi1)

dizi2=np.zeros((4,5))
print(dizi2)

dizi3=np.ones((3,5))*7
print(dizi3)

dizi4=np.arange(10,66,5)
print(dizi4)

dizi5=np.linspace(0,5,15)
print(dizi5)

dizi6=np.random.rand(15).reshape(3,5)
print(dizi6)

dizi7=np.eye(5)
print(dizi7)

dizi8=np.arange(24).reshape(4,6)
print(dizi8)

dizi9=np.random.rand(10)
print(dizi9.max())
print(dizi9.max())

dizi10=np.random.random(16).reshape(4,4)
print(dizi10)

print(dizi10[2,:])
print(dizi10[3,3])
print(dizi10[:,3])

for i in dizi10.flat:
    print(i)

dizi11=np.random.random(4)*5
print(dizi11)
print(dizi11.sum())
print(dizi11.std())
print(dizi11.var())
