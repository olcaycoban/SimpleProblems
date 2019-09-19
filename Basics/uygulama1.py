import numpy as np

a=np.array([1,2,3,4,56,7])
print(a)

print(type(a))

print(np.zeros((2,4)))

print(np.ones((4,4)))

print(np.ones((4,4))*5)

b=np.arange(10,40,5)
print(b)

c=np.arange(0,5,0.6)
print(c)

lin=np.linspace(10,20,8)
print(lin)

rast=np.random.rand(3,3)
print(rast)

norm=np.random.randn(3,3)
print(norm)

tamsayılar=np.random.randint(1,50,12)
print(tamsayılar)

stam=tamsayılar.reshape(4,3)
print(stam)

boyut3=tamsayılar.reshape(2,3,2)
print(boyut3)

print(tamsayılar.max())
print(tamsayılar.min())
print(tamsayılar.argmax())
print(tamsayılar.argmin())

tamsayılar.shape=2,-1,3
print(tamsayılar)
