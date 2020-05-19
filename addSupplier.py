from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import productManagement
import sqlite3
import styles

con = sqlite3.connect("products.db")
cur = con.cursor()

class AddSupplier(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Supplier")
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
        self.submitBtn.clicked.connect(self.insertSupplierData)
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.setStyleSheet(styles.buttonStyle2())
        self.cancelBtn.clicked.connect(self.cancel)
        self.addSupplierImg = QLabel()
        self.img = QPixmap('icons/addproduct.png')
        self.addSupplierImg.setPixmap(self.img)
        self.addSupplierImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Add Supplier")
        self.titleText.setStyleSheet(styles.titleStyle())
        #################################################
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter the name of Supplier")
        self.addressEntry = QLineEdit()
        self.addressEntry.setPlaceholderText("Enter the address of Supplier")

        self.cityEntry = QLineEdit()
        self.cityEntry.setPlaceholderText("Enter the city of Supplier")

        self.stateEntry = QLineEdit()
        self.stateEntry.setPlaceholderText("Enter the state of Supplier")

        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter the Mobile No of Supplier")

        self.gstEntry = QLineEdit()
        self.gstEntry.setPlaceholderText("Enter the GST No of Supplier")

        self.panEntry = QLineEdit()
        self.panEntry.setPlaceholderText("Enter the PAN No of Supplier")

        self.gstType = QComboBox()
        self.gstType.setStyleSheet(styles.comboStyle())
        self.gstType.addItem("Unregisterd")
        self.gstType.addItem("Regular")
        self.gstType.addItem("Composition")

        self.underGroup = QComboBox()
        self.underGroup.setStyleSheet(styles.comboStyle())
        self.underGroup.addItem("Commission A/C")
        self.underGroup.addItem("Assets A/C")
        self.underGroup.addItem("Bank A/C")
        self.underGroup.addItem("Cash in Hand A/C")
        self.underGroup.addItem("Capital A/C")
        self.underGroup.addItem("Defaulter A/C")
        self.underGroup.addItem("Delivery A/C")
        self.underGroup.addItem("Supplier A/C")
        self.underGroup.addItem("Expenses")
        self.underGroup.addItem("Investment")
        self.underGroup.addItem("Loan and Advance")
        self.underGroup.addItem("Opening Stock")
        self.underGroup.addItem("Sales A/C")
        self.underGroup.addItem("Purchase Expenses")
        self.underGroup.addItem("Sales Promotion")
        self.underGroup.addItem("Sallary Advance")
        self.underGroup.addItem("Duties and Taxes")
        self.underGroup.addItem("Secured Loan A/C")
        self.underGroup.addItem("Supplier A/C")
        self.underGroup.addItem("Credit A/C")
        self.underGroup.addItem("Unsecured Loans")
        ##################################################################################
        self.topLayout.addWidget(self.addSupplierImg)
        self.topLayout.addWidget(self.titleText)
        ##############################################################################
        self.bottomLayout.addRow(QLabel("Name :"),self.nameEntry)
        self.bottomLayout.addRow(QLabel("Address :"),self.addressEntry)
        self.bottomLayout.addRow(QLabel("City :"),self.cityEntry)
        self.bottomLayout.addRow(QLabel("State :"),self.stateEntry)
        self.bottomLayout.addRow(QLabel("Phone :"),self.phoneEntry)
        self.bottomLayout.addRow(QLabel("GST No :"),self.gstEntry)
        self.bottomLayout.addRow(QLabel("PAN No :"),self.panEntry)
        self.bottomLayout.addRow(QLabel("GST Type :"),self.gstType)
        self.bottomLayout.addRow(QLabel("Under Group :"),self.underGroup)
        self.bottomLayout.addRow(" ",self.submitBtn)
        self.bottomLayout.addRow(" ",self.cancelBtn)
        ###############################################################################
        self.layout.addLayout(self.topLayout)
        self.layout.addLayout(self.bottomLayout)
        self.setLayout(self.layout)

    def insertSupplierData(self):
        name = self.nameEntry.text()
        address = self.addressEntry.text()
        city = self.cityEntry.text()
        state = self.stateEntry.text()
        phone = self.phoneEntry.text()
        gst = self.gstEntry.text()
        pan = self.panEntry.text()
        gstType = self.gstType.currentText()
        underGroup = self.underGroup.currentText()

        if(name !=""):
            try:
                query = "INSERT INTO 'suppliers'(supplier_name,supplier_address,supplier_city,supplier_state,supplier_mobile,supplier_gst,supplier_pan,supplier_gst_type,supplier_group) VALUES(?,?,?,?,?,?,?,?,?) "
                cur.execute(query,(name,address,city,state,phone,gst,pan,gstType,underGroup))
                con.commit()
                QMessageBox.information(self, "Information", "Supplier has been added")
                self.close()
                self.window = productManagement.Main()
                self.window.show()

            except:
                QMessageBox.information(self, "Information", "Supplier has not been added")
        else:
            QMessageBox.information(self, "Information", "Please enter name of supplier")

    def cancel(self):
        self.close()
        self.window = productManagement.Main()
        self.window.show()



