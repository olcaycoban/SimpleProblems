from datetime import datetime
import os

suan=datetime.now()

zaman_damgasi=os.stat("..\..\Desktop\italya.txt").st_mtime
print(zaman_damgasi)

tarih=datetime.fromtimestamp(zaman_damgasi)
print(tarih)

suan_dakika=suan.minute
dosya_dakika=tarih.minute
print(type(tarih))
print(type(suan))
fark=suan_dakika-dosya_dakika
print(fark)
