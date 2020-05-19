from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import productManagement
import styles

con = sqlite3.connect("products.db")
cur = con.cursor()

class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 130, 450, 800)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.layout()
        self.widgets()

    def layout(self):
        self.layout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()

    def widgets(self):
        self.setStyleSheet("font-size:12pt")
        self.submitBtn = QPushButton("Submit")
        self.submitBtn.setStyleSheet(styles.buttonStyle())
        self.submitBtn.clicked.connect(self.insertItemData)
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.setStyleSheet(styles.buttonStyle2())
        self.cancelBtn.clicked.connect(self.cancel)
        self.addProductImg = QLabel()
        self.img = QPixmap('icons/addproduct.png')
        self.addProductImg.setPixmap(self.img)
        self.addProductImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Add Product")
        self.titleText.setStyleSheet(styles.titleStyle())
        #################################################
        self.productEntry = QLineEdit()
        self.productEntry.setPlaceholderText("Enter product name")
        self.hsnEntry = QLineEdit()
        self.cgstEntry = QLineEdit()
        self.sgstEntry = QLineEdit()
        self.igstEntry = QLineEdit()
        self.underGroup = QComboBox()
        self.underGroup.addItem("Tax Free")
        self.underGroup.addItem("3%")
        self.underGroup.addItem("5%")
        self.underGroup.addItem("12%")
        self.underGroup.addItem("18%")
        self.underGroup.addItem("28%")
        ##################################################################################
        self.topLayout.addWidget(self.addProductImg)
        self.topLayout.addWidget(self.titleText)
        ##############################################################################
        self.bottomLayout.addRow(QLabel("Product Name :"),self.productEntry)
        self.bottomLayout.addRow(QLabel("HSN :"),self.hsnEntry)
        self.bottomLayout.addRow(QLabel("CGST :"),self.cgstEntry)
        self.bottomLayout.addRow(QLabel("SGST :"),self.sgstEntry)
        self.bottomLayout.addRow(QLabel("IGST :"),self.igstEntry)
        self.bottomLayout.addRow(QLabel("Under Group :"),self.underGroup)
        self.bottomLayout.addRow(" ",self.submitBtn)
        self.bottomLayout.addRow(" ",self.cancelBtn)
        ###############################################################################
        self.layout.addLayout(self.topLayout)
        self.layout.addLayout(self.bottomLayout)
        self.setLayout(self.layout)

    def insertItemData(self):
        name = self.productEntry.text()
        hsn = self.hsnEntry.text()
        cgst = self.cgstEntry.text()
        sgst = self.sgstEntry.text()
        igst = self.igstEntry.text()
        group = self.underGroup.currentText()

        if(name != ""):
            try:
               query = "INSERT INTO 'products' (product_name,product_hsn,product_cgst,product_sgst,product_igst,product_group) VALUES(?,?,?,?,?,?)"
               cur.execute(query,(name,hsn,cgst,sgst,igst,group))
               con.commit()
               QMessageBox.information(self,"Information","Product has been added")
               self.close()
               self.window = productManagement.Main()
               self.window.show()

            except:
                QMessageBox.information(self, "Information", "Product has not been added")

        else:
            QMessageBox.information(self, "Information", "Please enter name")

    def cancel(self):
        self.close()
        self.window = productManagement.Main()
        self.window.show()
