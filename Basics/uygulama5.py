import numpy as np

a=np.random.random(15)
print(a)

print(np.mean(a))
print(np.median(a))
print(np.var(a))
print(np.std(a))
kopya=a.copy()
print(kopya)

sehirler=np.array(["istanbul","ankara","bursa","bursa","bursa","istanbul"])
print(np.unique(sehirler))
