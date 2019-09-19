import  numpy as np

dizi1=np.arange(10**2)
print(dizi1)

dizi1[1]=5000
print(dizi1[3:45])

print(dizi1[1])

dizi2=np.array((1,8,5,8,3,1,3,12,78))
for i in dizi2:
    print(2*i)

dizi3=np.random.randint(1,45,15)
print(dizi3)
dizi3=dizi3.reshape(3,5)
print(dizi3)
#print(dizi3.ravel()) diziyi eski haline getirir

print(dizi3[0:2,2])

#dizi4=np.random.random(16)
#print(dizi4)

print(dizi3[1:2,2])
print(dizi3[:,2])
