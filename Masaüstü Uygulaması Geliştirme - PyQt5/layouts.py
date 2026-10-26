import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True) #setAutoFillBackground:bir widget'ın (nesnenin) arka planının, atanan renk veya desenle otomatik olarak doldurulup doldurulmayacağını belirleyen komuttur.

        palette = self.palette() #palette():bir widget'ın renk paletine (arka plan, yazı rengi, buton rengi vb.) erişmeni sağlayan komuttur.
        palette.setColor(QPalette.Window, QColor(color)) #setColor:bir palet nesnesindeki (QPalette) belirli bir bölgenin (yazı, arka plan, buton vb.) rengini değiştirmek için kullanılan ana komuttur.
        self.setPalette(palette) #setPalette:hazırladığın veya üzerinde değişiklik yaptığın bir renk paletini (QPalette) ilgili widget'a resmen uygulamak ve giydirmek için kullanılan komuttur.

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)

        hlayout1 = QtWidgets.QHBoxLayout() #QHBoxLayout:içine eklenen widget'ları soldan sağa (yatay) doğru otomatik olarak yan yana dizen "Yerleşim Düzeni"dir.
        hlayout1.addWidget(Color('red'))
        hlayout1.addWidget(Color('blue'))
        hlayout1.addWidget(Color('green'))
        # hlayout1.setContentsMargins(30,20,0,30) #setConcentsMargins():İşlevi: Layout'un dört bir yanından (sol, üst, sağ, alt) içe doğru ne kadar boşluk bırakılacağını belirler.
        hlayout1.setSpacing(50) #setSpacing:bir yerleşim düzeni (Layout) içindeki nesnelerin (widget'ların) kendi aralarındaki boşluğu ayarlayan komuttur.

        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color('red'))
        hlayout2.addWidget(Color('green'))
        hlayout2.setSpacing(20)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        # layout = QtWidgets.QGridLayout() #QGridLayout:içine eklenen widget'ları bir satranç tahtası veya Excel tablosu gibi satırlar ve sütunlar (ızgara) halinde düzenleyen yerleşim sistemidir.

        # layout.addWidget(Color('red'),0,0) #1.satırdaki aşağı yukarı için. 2.satırdaki sayıda yan hareketlere doğru
        # layout.addWidget(Color('blue'),1,0) 
        # layout.addWidget(Color('green'),0,2) 
        # layout.addWidget(Color('yellow'),3,3) 

        widget = QWidget()
        widget.setLayout(vlayout) #setLayout:hazırladığın bir yerleşim düzenini (Layout) pencereye veya bir widget'a resmen monte eden komuttur.

        self.setCentralWidget(widget) #setCentralWidget:QMainWindow (Ana Pencere) tipindeki pencerelerde, pencerenin tam orta (merkez) alanını kaplayacak olan ana bileşeni belirleyen komuttur.

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()