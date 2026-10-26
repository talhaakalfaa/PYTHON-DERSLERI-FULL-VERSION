import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2



"""
figure = plt.figure() #figure:Grafiğin üzerine çizileceği boş tuvali (çerçeveyi) oluşturur.
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])Oluşturulan tuvalin (figure) içine, konumunu ve boyutunu tamamen sizin belirlediğiniz yeni bir grafik alanı (eksen) ekler.
[sol, alt, genişlik, yükseklik] = [0.1,0.1,0.8,0.8]

axes_cube.plot(x,y, 'b')
axes_cube.set_xlabel("X Axis")
axes_cube.set_xlabel("Y Axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z, 'r')
axes_square.set_xlabel("X Axis")
axes_square.set_xlabel("Y Axis")
axes_square.set_title("Square")
"""


"""
figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
plt.legend(loc=4) #loc=4:sağ altta çıkartır, 1 sağ üst, 2 sol üst, 3 sol alt.
"""
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")
plt.tight_layout()
# fig.savefig("figure1.png")
fig.savefig("figure1.pdf")

plt.show()