import sys #sys.argv, Python'un kendi sistem kütüphanesinden gelir ve komut satırı argümanlarını temsil eden bir listedir.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon
def window():
    app = QApplication(sys.argv) # QApplication:uygulamanın genel kontrol akışını ve ana ayarlarını yöneten sınıftır. Programın arka planındaki "yönetici" gibi düşünebilirsin.
    win = QMainWindow() # QMainWindow:uygulamanın gövdesidir.bu profesyonel pencereleri oluşturmak için özelleşmiş hazır bir şablondur.

    win.setWindowTitle('First Application') # win.setWindowTitle():oluşturduğun pencerenin en üstündeki başlık çubuğunda yazacak olan metni belirleyen komuttur.
    win.setGeometry(200,200,700,700) # win.setGeometry():pencerenin ekranın neresinde duracağını ve ne kadar büyük olacağını tek bir satırda belirleyen komuttur.
    win.setWindowIcon(QIcon('icon.png')) # win.setWindowIcon():pencerenin sol üst köşesinde ve görev çubuğunda (ekranın altındaki bar) görünecek olan logoyu/ikonu belirler.
    win.setToolTip('my tooltip') # win.setToolTip():kullanıcının faresini bir nesnenin (buton, yazı veya pencerenin kendisi) üzerine getirdiğinde beliren o küçük yardımcı bilgi kutucuğunu (ipucu) oluşturur.


    win.show() # win.show():hazırladığın tüm o kodları, pencereleri ve butonları ekranda görünür hale getiren komuttur.
    sys.exit(app.exec_())

window()

# app.exec_():"Olay döngüsünü" başlatır. Yani programın bir döngüye girip senin tıklamalarını, fare hareketlerini beklemesini sağlar. Bu satır olmazsa program saniyesinde açılıp kapanır.
# sys.exit():Pencereyi kapattığında işletim sistemine (Windows/Mac) "Tamam, program sorunsuz kapandı" mesajını gönderir ve bilgisayarın belleğini temizler.

# app = QApplication(sys.argv): Uygulama dünyasını yarat.
# win = QMainWindow(): Oyuncuları (pencere, buton) sahneye koy.
# win.show(): Perdeyi aç!
# sys.exit(app.exec_()): Seyirci (kullanıcı) salondan çıkana kadar bekle ve sonra ışıkları kapat.