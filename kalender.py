import calendar
bulan = int(input("masukan bulan : "))
tahun = int(input("masukan tahun : "))

if bulan > 12 or bulan < 0 and tahun < 0 or tahun > 9999:
  print("bulan dan tahun tidak valid")
elif bulan > 12 or bulan < 0 :
  print("bulan tidak valid")
elif tahun < 0 or tahun > 9999:
  print("tahun tidak valid")
else :
  print(calendar.month(tahun,bulan))