import numpy as np 

# result = np.array([1,3,5,7,9]) #birden fazla veriyi tek bir yapı içinde tutan dizidir.
# result = np.arange(1,10) #Belirli bir aralıkta, belli bir artışla sayılar üretir.
# result = np.arange(10,100,3)
# result = np.zeros(10) #tüm elemanları sıfırdan oluşan bir matris veya dizi oluşturmak için kullanılan bir komuttur.
# result = np.ones(10) #tüm elemanları birden oluşan bir matris veya dizi oluşturmak için kullanılan bir komuttur.
# result = np.linspace(0,100,5) #Belirlediğin bir başlangıç ve bitiş değeri arasında, birbirine tamamen eşit uzaklıkta sayılar üretir.
# result = np.linspace(0,5,5)
# result = np.random.randint(0,10) #Belirlediğiniz bir alt sınır (dahil) ve üst sınır (hariç) arasında, bilgisayar tarafından rastgele seçilmiş tam sayılar üretir.
# result = np.random.randint(20)
# result = np.random.randint(1,10,3)
# result = np.random.rand(5) #0 ile 1 arasında rastgele ondalıklı (float) sayılar üretmek için kullanılan bir fonksiyondur.
# result = np.random.randn(5) #Üretilen sayıların çoğu -1 ile 1 arasındadır.bu fonksiyonda negatif sayılar da üretilir.
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)
# print(np_multi.sum(axis=1)) #satırların toplamını verir
# print(np_multi.sum(axis=0)) #sütunların toplamını verir

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
# result = rnd_numbers.max() #sıralanan sayı içerisinden en büyüğü alır.
# result = rnd_numbers.min() #sıralanan sayı içerisinden en küçüğü alır.
# result = rnd_numbers.mean() #sıralanan sayıların ortalamasını alır.
# result = rnd_numbers.argmax() #sıralanan sayılar arasında en büyük olan sayının indisini verir.
# result = rnd_numbers.argmin() #sıralanan sayılar arasında en küçük olan sayının indisini verir.


print(result)