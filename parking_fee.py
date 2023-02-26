# 1 saate kadar: 4 TL
# 1-5 saat arası: Saat başı 5 TL
# # 5 saatten fazla: Saat başı 6 TL


saat = int(input("Burda kac saat vakit gecirdigizi girin: "))
ucret = 0
if saat < 1:
    ucret = 4
elif 1 < saat <= 5:
    ucret = 5 * saat
if saat > 5:
    ucret = 6 * saat

print("Odenmesi gereken miktar: {}TL" .format(ucret))
