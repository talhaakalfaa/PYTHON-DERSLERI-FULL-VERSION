from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _msgboxForm import Ui_MainWindow
import sys 

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.ShowDialog)

    def ShowDialog(self):

        result = QMessageBox.question(self, 'Close Application', 'Are you sure ?',QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes clicked')
            QtWidgets.qApp.quit()
        else:
            print('No clicked')



    #    msg = QMessageBox()

    #    msg.setWindowTitle('Close Application')
    #    msg.setText('Are you sure ?')
    #    msg.setIcon(QMessageBox.Warning) # QMessageBox, kullanıcıya önemli bir bilgi vermek, bir uyarıda bulunmak veya bir onay almak (Evet/Hayır gibi) için açılan **"Küçük İletişim Penceresi"**dir.
    #    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore) #setStandardButtons:bir mesaj kutusunda (QMessageBox) kullanıcının karşısına hangi butonların (Tamam, İptal, Evet, Hayır vb.) çıkacağını belirleyen komuttur.
    #    msg.setDefaultButton(QMessageBox.Cancel) # setDefaultButton, bir mesaj kutusu (QMessageBox) açıldığında hangi butonun "varsayılan" (ön tanımlı) olacağını belirleyen komuttur.
    #    msg.setDetailedText('details....') # setDetailedText, bir mesaj kutusunda (QMessageBox) ilk bakışta görünmeyen, ancak kullanıcı "Show Details..." (Detayları Göster) butonuna tıkladığında açılan ekstra bir metin alanı ekler.
    #    msg.buttonClicked.connect(self.popup_button)
       
    #    x = msg.exec_()
    #    print(x)


    # def popup_button(self, i):
    #     print(i.text())

    #     if i.text() == 'OK':
    #         print('OKEY')
    #         QtWidgets.qApp.quit() #OK'a basınca açılan uygulamayı kapatan kod.
    #     elif i.text() == 'Cancel':
    #         print('Cancel...')
    #     else:
    #         print('Ignore')

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()