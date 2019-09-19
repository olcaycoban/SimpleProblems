from _datetime import datetime

print(datetime.now())
print(datetime.now().time())
suan=datetime.now()

print(suan.year)
print(suan.time())
print(suan.date())
tarih=str(suan.date())
print(tarih.split("-"))

print(datetime.ctime(suan))
