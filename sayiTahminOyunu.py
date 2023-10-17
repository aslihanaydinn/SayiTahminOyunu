import random
number = random.randint(1,100)
puan = 100
hakSayisi = int(input("Kaç hakkınız olsun?"))
for i in range(hakSayisi):
    temp = int(input("Tahmininizi girin: "))
    if (temp < number):
        print("Yukarı")
        puan = puan -20
        if(puan == 0):
            break
    elif(temp > number):
        print("Aşağı")
        puan = puan - 20
        if(puan == 0):
            break
    else:
        print("Tebrikler sayıyı doğru tahmin ettiniz!")
        print(f'puanınız: {puan}')
        break
print(f'Tahmin hakkınız bitti. Sayı: {number} idi.')