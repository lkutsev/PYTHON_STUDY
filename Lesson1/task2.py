# 1
s = int(input('Введите количество секунд:'))
hh = int(s/3600)
mm = int((s - (hh*3600))/60)
ss = int(s - (hh*3600) - (mm*60))
print('вариант 1: %02d:%02d:%02d'%(hh,mm,ss))
#2
hh = s//3600
mm = (s%3600)/60
ss = s%60
print('вариант 1: %02d:%02d:%02d'%(hh,mm,ss))
##print(f'{s:%H:%M:%S}')