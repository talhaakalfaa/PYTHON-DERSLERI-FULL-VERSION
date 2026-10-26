import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"--r",linewidth ="5") #-- kesik şekilde çizgi oluşturur r=red.
plt.plot(x,y,color = "green",linewidth ="5") #linewidth:çizgi kalınlığını ayarlar.
plt.plot(x,y,"o--y") # o:x ile y nin kesişim noktalarına işaret koyar.
plt.axis([0,6,0,20]) # ilk iki rakam x ekseni,diğer iki rakam y ekseni başlangıç ve bitiş noktalarıdır.

plt.plot(...) #plot:çizgi grafiği (line plot) oluşturmaya yarayan en temel fonksiyondur.

plt.title("Grafik Başlığı") #title:başlık (isim) eklemeye yarar
plt.xlabel("x label") #xlabel:yatay eksenine (X ekseni) bir açıklama metni eklemeye yarar
plt.ylabel("y label") #ylabel:dikey eksenine (Y ekseni) bir açıklama metni eklemeye yarar.
"""


"""
x = np.linspace(0,2,100)

plt.plot(x, x, label="linear",color ="blue")#label:hangi çizginin neyi temsil ettiğini bilgisayara tanıtmış olursun.
plt.plot(x, x**2, label="quadratic",color="yellow")
plt.plot(x, x**3, label="cubic",color="green") 

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("simple plot")

plt.legend() #legend():hangi rengin veya şeklin hangi veriye ait olduğunu anlamamızı sağlar.

plt.show() #show():grafiği ekranda görüntüleyen son komuttur.
"""

"""
fig,axs = plt.subplots(3) #subplots:birden fazla grafik paneli oluşturmaya yarar.

axs[0].plot(x, x, color ="red")
axs[0].set_title("linear") #set_title:her bir küçük grafiğe (panel) ayrı ayrı başlık vermeni sağlar.

axs[1].plot(x, x**2, color ="green")
axs[1].set_title("quadratic")

axs[2].plot(x, x**3, color ="yellow")
axs[2].set_title("cubic")

plt.tight_layout() #plt.tight_layout():Grafiklerin birbirine girmesini engelleyen, otomatik bir "hizalama ve düzenleme" komutudur.
"""


"""
x = np.linspace(0,2,100)

fig,axs = plt.subplots(2,2) #(2,2) 2 satır 2 sütun oluşturur
fig.suptitle("grafik başlığı")

axs[0,0].plot(x, x, color ="red")
axs[0,1].plot(x, x**2, color ="blue")
axs[1,0].plot(x, x**3, color ="green")
axs[1,1].plot(x, x**4, color ="yellow")
"""

import pandas as pd

df = pd.read_csv("nba.csv")


df = df.drop(["Number"], axis = 1).groupby("Team").mean(numeric_only=True)
df.plot(subplots=True)
plt.legend()

plt.show()