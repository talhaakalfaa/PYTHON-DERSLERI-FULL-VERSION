import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('First Application')
        self.setGeometry(200,200,700,700)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('my tooltip')
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('Adınız: ')
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Soyadınız: ')
        self.lbl_surname.move(50,70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,150)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32) #resize:bir nesnenin (widget) boyutlarını manuel olarak yeniden ayarlamak için kullanılan komuttur.


        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Giriş')
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked)
    
    def clicked(self):
        self.lbl_result.setText('ad: '+self.txt_name.text()+ ' soyad: '+ self.txt_surname.text())

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    
    win.show()
    sys.exit(app.exec_())

window()


# QLabel:Kullanıcının değiştiremediği, sadece okuduğu veya gördüğü her şeyi bununla yaparsın.
# QComboBox:Ekran üzerinde çok az yer kaplayan, tıklandığında aşağı doğru bir seçenek listesi açan ve kullanıcının bu listeden tek bir seçim yapmasını sağlayan araçtır.
# QCheckBox:Bir seçeneği seçmek veya seçimden kaldırmak için kullanılır (Örn: "Beni Hatırla" veya "Kullanım Koşullarını Kabul Ediyorum").
# QRadioButton:Birden fazla seçenek arasında "ya o, ya bu" mantığıyla çalışır (Örn: Cinsiyet seçimi, Ödeme yöntemi seçimi).
# QPushButton:kullanıcının üzerine tıklayarak bir işlemi başlattığı en temel **"Komut Butonu"**dur.
# QTableWidget:Veritabanı kayıtları, listeler veya karmaşık verileri ızgara yapısında sunmak ve düzenlemek için kullanılır.
# QlineEdit:Kullanıcıdan isim, şifre, e-posta veya arama terimi gibi kısa bilgileri almak için kullanılır.
# QSlider:Sayısal bir değeri (0-100 arası gibi) fare ile sürükleyerek hızlıca ayarlamak için kullanılır (Örn: Ses seviyesi, Ekran parlaklığı).
# QProgressBar:Uzun süren işlemlerin (dosya indirme, yükleme, hesaplama gibi) aşamasını yüzde (%) olarak canlı bir şekilde göstermek için kullanılır.