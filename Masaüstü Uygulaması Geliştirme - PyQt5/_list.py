import sys 
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from PyQt5 import QtWidgets
from _listForm import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load Students 
        self.loadStudents()

        # add new student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        # edit student 
        self.ui.btnEdit.clicked.connect(self.editStudent)

        # delete student
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        # up student
        self.ui.btnUp.clicked.connect(self.upStudent)

        #down student
        self.ui.btnDown.clicked.connect(self.downStudent)

        # sort
        self.ui.btnSort.clicked.connect(self.sortStudents)

        # close
        self.ui.btnExit.clicked.connect(self.close)


    def loadStudents(self):
        self.ui.listItems.addItems(['Talha','Çağan','İlknur'])
        self.ui.listItems.setCurrentRow(0) #setCurrentRow:bir QListWidget (liste kutusu) içindeki belirli bir satırı kod yazarak seçili hale getirmeni sağlayan komuttur.
    
    
    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow() #currentRow():bir QListWidget (liste kutusu) içerisinde kullanıcının o an hangi satırı seçtiğini öğrenmeni sağlayan komuttur.
        text, ok = QInputDialog.getText(self, "New Student", "Student Name" ) #QInputDialog:kullanıcıdan hızlı bir şekilde tek bir veri (metin, sayı veya listeden bir seçim) almak için kullanılan en pratik hazır iletişim kutusu sınıfıdır.
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex , text) #insertItem:bir QListWidget veya QComboBox (liste yapıları) içerisine, yeni bir elemanı listenin en sonuna değil, senin istediğin özel bir sıraya (indekse) yerleştiren komuttur.

    def editStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    def removeStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        
        if item is None:
            return
        
        q = QMessageBox.question(self, "Remove Student", "Do you want to remove student: " + item.text(), QMessageBox.Yes | QMessageBox.No) #QMessageBox.question, kullanıcıya bir soru sorup, ondan "Evet" veya "Hayır" gibi bir cevap bekleyen hazır bir mesaj kutusu yöntemidir.
        if q == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item
    
    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index >= 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item) #setCurrentItem, bir QListWidget (liste kutusu) içindeki belirli bir maddeyi (item) nesne olarak hedef alıp kod yazarak seçili hale getirmeni sağlayan komuttur.


    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count()-1: #Bu kod satırındaki count(), listenin "bitiş çizgisini" belirlemek için kullanılmıştır.
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, item)
            self.ui.listItems.setCurrentItem(item)

    def sortStudents(self):
        self.ui.listItems.sortItems()

    def close(self):
        quit()



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()