from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import styles
con = sqlite3.connect("products.db")
cur = con.cursor()

class Stock(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 160, 400, 400)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.layout()
        self.widgets()

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
    def widgets(self):
        self.setStyleSheet("font-size:12pt;background-color:moccasin")
        self.stockImg = QLabel()
        self.img = QPixmap('images/images10.jpg')
        self.stockImg.setPixmap(self.img)
        self.titleText = QLabel("Stock Details")
        self.titleText.setStyleSheet(styles.titleStyle())

        self.productCombo = QComboBox()
        self.productCombo.setStyleSheet(styles.comboStyle())
        self.stockLbl = QLabel()

        self.btn = QPushButton("Close")
        self.btn.setStyleSheet(styles.buttonStyle())
        self.btn.clicked.connect(self.cancel)
        self.topLayout.addWidget(self.stockImg)
        self.topLayout.addWidget(self.titleText)
        self.bottomLayout.addRow(QLabel("Product :"),self.productCombo)
        self.bottomLayout.addRow(QLabel("Stock :"),self.stockLbl)
        self.bottomLayout.addWidget(self.btn)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

        query = "SELECT product_id ,product_name FROM products"
        products = cur.execute(query).fetchall()

        for product in products:
            self.productCombo.addItem(product[1], product[0])

        self.productCombo.activated.connect(self.valueChanged)

    def valueChanged(self):
        try:
            item = self.productCombo.currentText()
            itemId = self.productCombo.currentData()

            query = "SELECT stock FROM stock WHERE product = ? AND product_id = ?"
            ok = cur.execute(query,(item,itemId)).fetchone()
            self.stockLbl.setText(str(ok[0]))
        except:
            QMessageBox.information(self,"Information",item +" is Out of Stock")


    def cancel(self):
        self.close()



