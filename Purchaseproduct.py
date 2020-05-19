from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import styles
import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

class PurchaseProducts(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Purchase Bill")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(280, 130, 1150, 800)

        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.layout()
        self.Widgets()

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.Layout = QVBoxLayout()
        self.firstLayot = QHBoxLayout()
        self.layout1 = QVBoxLayout()
        self.layout2 = QFormLayout()
        self.layout3 = QFormLayout()
        self.layout4 = QFormLayout()
        self.layout5 = QFormLayout()
        self.layout6 = QFormLayout()
        self.layout7 = QHBoxLayout()
        self.layout8 = QFormLayout()
        self.layout9 = QVBoxLayout()
        self.layout10 = QHBoxLayout()
        self.layoutA = QHBoxLayout()
        self.layoutB = QHBoxLayout()
        self.layoutC = QHBoxLayout()
        self.layoutD = QHBoxLayout()
        self.layoutE = QHBoxLayout()
        self.layoutF = QHBoxLayout()
        self.layoutAmt = QHBoxLayout()
        self.layoutJoin = QHBoxLayout()
        self.layoutStock = QFormLayout()

    def Widgets(self):
        self.setStyleSheet("font-size:12pt")
        self.firmName = QLabel("Tulsi Sales")
        self.firmName.setStyleSheet(styles.firmStyle())
        self.date = QLabel("Date :")
        self.dateEntry = QDateTimeEdit()
        self.billNo = QLabel("Bill No :")
        self.billNoEntry = QLineEdit()

        self.agent = QLabel("Agent :")
        self.agentEntry = QLineEdit()


        self.pay = QLabel("Payment mode :")
        self.payCombo = QComboBox()
        self.payCombo.setStyleSheet(styles.comboStyle())
        self.payCombo.addItem("Cash")
        self.payCombo.addItem("Credit")
        self.payCombo.addItem("Cheque")
        self.supplier = QLabel("Supplier :")
        self.supplierCombo = QComboBox()
        self.supplierCombo.setStyleSheet(styles.comboStyle())
        self.product = QLabel("Product")
        self.productCombo = QComboBox()
        self.productCombo.setStyleSheet(styles.comboStyle())
        self.productCombo.currentTextChanged.connect(self.valueChanged)

        self.cgstLabel = QLabel("CGST")
        self.cgstEntry = QLineEdit()
        self.sgstLabel = QLabel("SGST")
        self.sgstEntry = QLineEdit()
        self.roundFigureLabel = QLabel("Round Figure")
        self.roundEntry = QLineEdit()
        self.finalTotal = QLabel("Total Amount")
        self.finalTotalEntry = QLineEdit()
        self.newBtn = QPushButton("Add New")
        self.newBtn.setStyleSheet(styles.buttonStyle4())
        self.newBtn.setFixedHeight(60)
        self.viewBtn = QPushButton("View Bill")
        self.viewBtn.setStyleSheet(styles.buttonStyle4())
        self.viewBtn.setFixedHeight(60)
        self.closeBtn = QPushButton("Close")
        self.closeBtn.setStyleSheet(styles.buttonStyle4())
        self.closeBtn.setFixedHeight(60)

        self.layout1.addWidget(self.firmName)
        self.layout1.addStretch()
        self.layout2.addRow(self.date, self.dateEntry)
        self.layout2.addRow(self.billNo, self.billNoEntry)

        self.layout3.addRow(self.agent, self.agentEntry)
        self.layout3.addRow(self.pay, self.payCombo)
        self.layoutB.addStretch()
        self.layoutA.addLayout(self.layout4, 45)
        self.layoutA.addLayout(self.layoutB, 55)
        self.layout4.addRow(self.supplier, self.supplierCombo)

        self.layoutC.addStretch()
        self.layoutD.addLayout(self.layout5, 45)
        self.layoutD.addLayout(self.layoutC, 55)

        self.firstLayot.addLayout(self.layout1, 50)
        self.firstLayot.addLayout(self.layout2, 25)
        self.firstLayot.addLayout(self.layout3, 25)

        self.hsnEntry = QLineEdit()
        self.quantityEntry = QLineEdit()
        self.netRateEntry = QLineEdit()
        self.rateEntry = QLineEdit()
        self.float = QDoubleValidator()
        self.taxEntry = QLineEdit()
        self.discEntry = QLineEdit()
        self.totalEntry = QLineEdit()
        self.addItemBtn = QPushButton("Add Item")
        self.addItemBtn.setStyleSheet(styles.buttonStyle2())
        self.addItemBtn.clicked.connect(self.addItem)
        self.totalBtn = QPushButton("Confirm")
        self.removeItemBtn = QPushButton("Remove Item")
        self.removeItemBtn.setStyleSheet(styles.buttonStyle2())
        self.removeItemBtn.clicked.connect(self.removeItem)

        self.layout6.addRow(QLabel("Product :"), self.productCombo)
        self.layout6.addRow(QLabel("HSN :"), self.hsnEntry)
        self.layout6.addRow(QLabel("Quantity :"), self.quantityEntry)
        self.layout6.addRow(QLabel("Rate :"), self.rateEntry)
        self.layout6.addRow(QLabel("Net Rate :"), self.netRateEntry)
        self.layout6.addRow(QLabel("Taxes :"), self.taxEntry)
        self.layout6.addRow(QLabel("Discount :"), self.discEntry)
        self.layout6.addRow(QLabel("Total :"), self.totalEntry)
        self.layout6.addRow(QLabel(""), self.addItemBtn)
        self.layout6.addRow(QLabel(""), self.removeItemBtn)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Product"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Quantity"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Net Rate"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Rate"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Total"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("CGST"))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem("SGST"))

        self.amountEntry = QLineEdit()

        self.layout7.addWidget(self.table)
        self.layoutAmt.addWidget(QLabel("Amount"))
        self.layoutAmt.addWidget(self.amountEntry)
        self.layoutAmt.setContentsMargins(450,10,10,20)
        self.layoutStock.addRow(QLabel("Stock :"))
        self.Layout.addLayout(self.layout7)
        self.layoutJoin.addLayout(self.layoutStock)
        self.layoutJoin.addLayout(self.layoutAmt)
        self.Layout.addLayout(self.layoutJoin)

        self.layoutE.addLayout(self.layout6, 20)
        self.layoutE.addLayout(self.layout9, 10)
        self.layoutE.addLayout(self.Layout, 70)

        self.layout8.addRow(self.cgstLabel, self.cgstEntry)
        self.layout8.addRow(self.sgstLabel, self.sgstEntry)
        self.layout8.addRow(self.roundFigureLabel, self.roundEntry)
        self.layout8.addRow(self.finalTotal, self.finalTotalEntry)

        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet(styles.buttonStyle4())
        self.saveBtn.clicked.connect(self.Save)
        self.saveBtn.setFixedHeight(60)

        self.layout10.addWidget(self.saveBtn)
        self.layout10.addWidget(self.addItemBtn)
        self.layout10.addWidget(self.newBtn)
        self.layout10.addWidget(self.viewBtn)
        self.layout10.addWidget(self.closeBtn)

        self.layoutF.addLayout(self.layout10,75)
        self.layoutF.addLayout(self.layout8,25)

        self.mainLayout.addLayout(self.firstLayot)
        self.mainLayout.addLayout(self.layoutA)
        self.mainLayout.addLayout(self.layoutD)
        self.mainLayout.addLayout(self.layoutE)
        self.mainLayout.addLayout(self.layoutF)

        self.setLayout(self.mainLayout)
        try:
            query1 = ("SELECT product_id ,product_name,product_hsn,"
                  "product_igst,product_group FROM products")
            products = cur.execute(query1).fetchall()

            self.tax = products[0][4]
            self.igst = products[0][3]
            self.hsn = products[0][2]
        except:
            QMessageBox.information(self, "Information", "Unable to process info")
        query2 = ("SELECT supplier_id ,supplier_name FROM suppliers")
        suppliers = cur.execute(query2).fetchall()

        for product in products:
            self.productCombo.addItem(product[1], product[0])

        for supplier in suppliers:
            self.supplierCombo.addItem(supplier[1], supplier[0])

        self.rateEntry.setMaxLength(7)
        self.totalEntry.setMaxLength(8)
        self.rateEntry.setMaxLength(7)
        self.cgstEntry.setMaxLength(5)
        self.sgstEntry.setMaxLength(5)
        self.finalTotalEntry.setMaxLength(7)
    ################################################################
        self.billNo = ("***")
        self.billNoEntry.setText(str(self.billNo))
        self.dateEntry.setDate(QDate.currentDate())
        self.dateEntry.setDisplayFormat("dd/MM/yyyy")

        self.viewBtn.clicked.connect(self.viewBill)
        self.newBtn.clicked.connect(self.newBill)
        self.closeBtn.clicked.connect(self.cancel)

    def valueChanged(self):
        productId = self.productCombo.currentData()
        query = ("SELECT product_group,product_hsn FROM products WHERE product_id = ?")
        taxes = cur.execute(query, (productId,)).fetchone()
        self.taxEntry.setText(str(taxes[0]))
        self.hsnEntry.setText(str(taxes[1]))

    def addItem(self):
        try:
            self.originalPrice = float(self.rateEntry.text())
            self.taxAmount = 2*(float(self.igst))
            self.netRateCalc = self.originalPrice + (self.originalPrice*(self.taxAmount/100))
            self.netRateEntry.setText(str(self.netRateCalc))

            self.calculate = float(self.quantityEntry.text()) * float(self.rateEntry.text())
            self.totalEntry.setText(str(self.calculate))

            self.gstAmt = float(self.netRateEntry.text()) - float(self.originalPrice)
            self.r = (float(self.gstAmt) * 100)/ float(self.netRateEntry.text())
            self.gstActual = self.r*float(self.quantityEntry.text())

            self.cgstEntry.setText(str((self.gstActual)/2))
            self.sgstEntry.setText(str((self.gstActual)/2))
            product = self.productCombo.currentText()
            productId = self.productCombo.currentData()
            supplierId = self.supplierCombo.currentData()
            hsn = self.hsnEntry.text()
            quantity = float(self.quantityEntry.text())
            net_rate = float(self.netRateEntry.text())
            rate = float(self.rateEntry.text())
            taxes = self.taxEntry.text()
            total = float(self.totalEntry.text())
            cgst = float(self.cgstEntry.text())
            sgst = float(self.sgstEntry.text())
            agent = self.agentEntry.text()
            payment_mode = self.payCombo.currentText()
            date = self.dateEntry.text()
            supplier = self.supplierCombo.currentText()
            stock = quantity
            try:
                query = ("INSERT INTO 'purchase' (supplier_id,products,hsn,quantity,net_rate,rate,tax,total,cgst,sgst,"
                                 "agent,payment_mode,date,supplier,stock)"
                                 " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
                cur.execute(query,(supplierId,product,hsn,quantity,net_rate,rate,taxes,total,cgst,sgst,
                                 agent,payment_mode,date,supplier,stock))
                con.commit()

            except:
                QMessageBox.information(self, "Information", "Failed to store information")

            try:
                query1 = ("INSERT INTO 'stock' (product_id,product,stock) VALUES (?,?,?)")
                cur.execute(query1,(productId,product,quantity))
                con.commit()
            except:
                QMessageBox.information(self, "Information", "Unable to update stock")
            self.tableDisplay()
            self.quantityEntry.setText("")
            self.netRateEntry.setText("")
            self.rateEntry.setText("")
            self.discEntry.setText("")
            self.totalEntry.setText("")
        except:
            QMessageBox.information(self, "Information", "Please fill up the fields")


    def tableDisplay(self):
        self.gstList = []
        self.sumList = []
        supplierId = self.supplierCombo.currentData()
        date = self.dateEntry.text()

        query = "SELECT products, quantity, net_rate, rate, total, cgst, sgst from purchase " \
                "WHERE supplier_id=? AND date=?"
        ok = cur.execute(query,(supplierId,date)).fetchall()

        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)

        for row_data in ok:
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.sumList.append(float(row_data[4]))
            self.gstList.append(float(row_data[5]))

            self.SUM = sum(self.sumList)
            self.gstTotal = sum(self.gstList)

            self.table.cellDoubleClicked.connect(self.doubleClicked)
            self.amountEntry.setText(str(self.SUM))
            self.cgstEntry.setText(str(self.gstTotal))
            self.sgstEntry.setText(str(self.gstTotal))

    def doubleClicked(self):
        row = self.table.currentRow()
        item = self.table.item(row,0).text()
        qty = self.table.item(row,1).text()
        nRate = self.table.item(row,2).text()
        rate = self.table.item(row,3).text()
        total = self.table.item(row,4).text()
        cgst = self.table.item(row,5).text()
        sgst = self.table.item(row,6).text()
        self.productCombo.setCurrentText(item)
        self.quantityEntry.setText(str(qty))
        self.rateEntry.setText(str(rate))
        self.totalEntry.setText(str(total))
        self.netRateEntry.setText(str(nRate))
        self.cgstEntry.setText(str(cgst))
        self.sgstEntry.setText(str(sgst))
        self.updateFun()
        ###########################################
    def updateFun(self):
        supplierId = self.supplierCombo.currentData()
        product = self.productCombo.currentText()
        quantity = float(self.quantityEntry.text())
        date = self.dateEntry.text()
        try:
            query = "DELETE FROM purchase WHERE products = ? AND supplier_id =? AND date = ? AND quantity =?"
            cur.execute(query, (product, supplierId, date, quantity))
            con.commit()
        except:
            QMessageBox.information(self, "Information", "Unable to Update")

        for purchase in range(self.table.rowCount()):
            self.table.update()

    def removeItem(self):
        try:
            curRow = self.table.currentRow()
            supplierId = self.supplierCombo.currentData()
            quantity = (self.table.item(curRow,1).text())
            date = self.dateEntry.text()
            item = self.table.item(curRow,0).text()
            qty = float(quantity)
            try:
                query = "DELETE FROM purchase WHERE products = ? AND supplier_id =? AND date = ? AND quantity =?"
                cur.execute(query, (item, supplierId, date, qty))
                con.commit()
            except:
                QMessageBox.information(self, "Information", "Unable to remove")
            self.table.removeRow(curRow)
        except:
            QMessageBox.information(self, "Information", "Select s item")

    def Save(self):
        try:
            date = self.dateEntry.text()
            supplierId = self.supplierCombo.currentData()

            self.final = (float(self.cgstEntry.text()) + float(self.sgstEntry.text()) + float(self.amountEntry.text()))
            self.finalTotalEntry.setText(str(round(self.final)))
            ##############################################################
            query = ("INSERT INTO 'bills' (supplier_id,date) VALUES (?,?)")
            cur.execute(query, (supplierId, date))
            con.commit()
            query1 = "SELECT billnoId FROM bills WHERE supplier_id =? AND date =?"
            ok = cur.execute(query1,(supplierId,date)).fetchone()
            bill = ok[0]
            self.billNoEntry.setText(str(bill))
            amount = float(self.amountEntry.text())
            cgst = (float(self.cgstEntry.text()))
            sgst = (float(self.sgstEntry.text()))
            total_amount = (float(self.finalTotalEntry.text()))

            query2 = "UPDATE purchase SET billnoId =?, amount =?, total_cgst =?, total_sgst =?, total_amount =?" \
                     " WHERE supplier_id =? AND date =?"
            cur.execute(query2,(bill,amount,cgst,sgst,total_amount,supplierId,date))
            con.commit()

            self.stockMaintain()
        except:
            QMessageBox.information(self, "Information", "Add the products first")


    def viewBill(self):
        self.bill = viewBills()
    def newBill(self):
        self.close()
        self.main = PurchaseProducts()
    def cancel(self):
        self.close()

    def stockMaintain(self):
        product = self.productCombo.currentText()
        productId = self.productCombo.currentData()
        try:
            query = "SELECT quantity FROM purchase WHERE products = ?"
            ok = cur.execute(query,(product,)).fetchall()
            print(ok)
            stock = []
            for tuple in ok:
                listt = list(tuple)
                for m in listt:
                    stock.append(m)
            final = sum(stock)

            query2 = "UPDATE stock SET stock =? WHERE product_id = ? AND product = ?"
            cur.execute(query2,(final,productId, product))
            con.commit()
        except:
            QMessageBox.information(self, "Information", "Sorry, Failed to update stock")

class viewBills(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Billing Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(180, 130, 1700, 800)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.layout()
        self.widgets()

    def layout(self):
        self.finalLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()

        self.mainLayout = QVBoxLayout()
        self.firstLayot = QHBoxLayout()
        self.layout1 = QVBoxLayout()
        self.layout2 = QFormLayout()
        self.layout3 = QFormLayout()
        self.layout4 = QFormLayout()
        self.layout5 = QVBoxLayout()
        self.layout6 = QHBoxLayout()
        self.layout8 = QFormLayout()
        self.layoutBtns = QHBoxLayout()
        self.layoutAdj = QHBoxLayout()
        self.layoutEmp = QHBoxLayout()

    def widgets(self):
        self.setStyleSheet("font-size:12pt")
        self.firmName = QLabel("Tulsi Sales")
        self.firmName.setStyleSheet(styles.firmStyle())
        self.date = QLabel("Date :")
        self.dateEntry = QLineEdit()
        self.billNo = QLabel("Bill No :")
        self.billNoEntry = QLineEdit()

        self.dateCombo = QComboBox()
        self.dateCombo.setStyleSheet(styles.comboStyle())

        self.agent = QLabel("Agent :")
        self.agentEntry = QLineEdit()


        self.pay = QLabel("Payment mode :")
        self.payEntry = QLineEdit()

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Product"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("HSN"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Qty"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Net Rate"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Rate"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("Taxes"))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem("Discount"))
        self.table.setHorizontalHeaderItem(7, QTableWidgetItem("Total"))

        self.layout1.addWidget(self.firmName)
        self.layout1.addStretch()
        self.layout2.addRow(self.agent, self.agentEntry)

        self.layout3.addRow(self.date, self.dateCombo)
        self.layout3.addRow(self.billNo, self.billNoEntry)
        self.layout3.addRow(self.pay, self.payEntry)

        self.supplier = QLabel("Supplier :")
        self.suppliercombo = QLineEdit()

        self.cgstLabel = QLabel("CGST")
        self.cgstEntry = QLineEdit()
        self.sgstLabel = QLabel("SGST")
        self.sgstEntry = QLineEdit()
        self.roundFigureLabel = QLabel("Round Figure")
        self.roundEntry = QLineEdit()
        self.finalTotal = QLabel("Total Amount")
        self.finalTotalEntry = QLineEdit()

        self.amountEntry = QLineEdit()

        self.firstLayot.addLayout(self.layout1, 50)
        self.firstLayot.addLayout(self.layout2, 25)
        self.firstLayot.addLayout(self.layout3, 25)

        self.layout4.addRow(self.supplier, self.suppliercombo)
        self.layout4.setContentsMargins(10, 10, 700, 10)

        self.table.setFixedSize(1100, 300)
        self.layout5.addWidget(self.table)
        self.layout5.setContentsMargins(10, 0, 50, 10)

        self.layout6.addWidget(QLabel("Amount"))
        self.layout6.addWidget(self.amountEntry)
        self.layout6.setContentsMargins(750, 10, 150, 50)

        self.layout8.addRow(self.cgstLabel, self.cgstEntry)
        self.layout8.addRow(self.sgstLabel, self.sgstEntry)
        self.layout8.addRow(self.roundFigureLabel, self.roundEntry)
        self.layout8.addRow(self.finalTotal, self.finalTotalEntry)
        self.upadteBtn = QPushButton("Update")
        self.upadteBtn.setStyleSheet(styles.buttonStyle3())
        self.upadteBtn.setFixedSize(200,100)
        self.upadteBtn.clicked.connect(self.updateBill)
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.setStyleSheet(styles.buttonStyle3())
        self.deleteBtn.setFixedSize(200,100)
        self.deleteBtn.clicked.connect(self.deleteBill)
        self.closeBtn = QPushButton("Close")
        self.closeBtn.setStyleSheet(styles.buttonStyle3())
        self.closeBtn.setFixedSize(200,100)
        self.closeBtn.clicked.connect(self.cancel)

        self.list = QListWidget()
        self.layoutBtns.addWidget(self.upadteBtn)
        self.layoutBtns.addWidget(self.deleteBtn)
        self.layoutBtns.addWidget(self.closeBtn)
        self.layoutEmp.addWidget(QLabel(""))
        self.layoutAdj.addLayout(self.layoutBtns,70)
        self.layoutAdj.addLayout(self.layoutEmp,10)
        self.layoutAdj.addLayout(self.layout8,20)
        self.mainLayout.addLayout(self.firstLayot)
        self.mainLayout.addLayout(self.layout4)
        self.mainLayout.addLayout(self.layout5)
        self.mainLayout.addLayout(self.layout6)
        self.mainLayout.addLayout(self.layoutAdj)
        self.rightLayout.addWidget(self.list)

        self.finalLayout.addLayout(self.mainLayout, 75)
        self.finalLayout.addLayout(self.rightLayout, 25)

        self.setLayout(self.finalLayout)

        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)

        query = "SELECT supplier_id,supplier_name FROM suppliers"
        cust = cur.execute(query).fetchall()
        for suppliers in cust:
            self.list.addItem(str(suppliers[0]) + "-" + str(suppliers[1]))

        self.list.itemDoubleClicked.connect(self.doubleClicked)
        #####################################################################
        self.table.setFont(QFont("times", 12))
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def doubleClicked(self):
        self.dateCombo.clear()

        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)
        global supplierID

        supplier = self.list.currentItem().text()
        supplierID = supplier.split("-")[0]
        supplierName = supplier.split("-")[1]
        self.suppliercombo.setText(supplierName)
        try:
            query = ("SELECT date FROM bills WHERE supplier_id = ?")
            show = cur.execute(query, (supplierID,)).fetchall()
        except:
            QMessageBox.information(self,"Information","Failed to load date")

        for data in show:
            self.dateCombo.addItem(str(data[0]))
        self.dateCombo.activated.connect(self.display)


    def display(self):
        supplier = self.list.currentItem().text()
        supplierId = supplier.split("-")[0]
        date = self.dateCombo.currentText()
        try:
            query2 = "SELECT  billnoId, amount, total_cgst, total_sgst, total_amount, payment_mode FROM purchase" \
                 " WHERE supplier_id =?"
            show = cur.execute(query2, (supplierId,)).fetchone()
        except:
            QMessageBox.information(self,"Information","Failed to load information")
        bill = show[0]
        amount = show[1]
        cgst = show[2]
        sgst = show[3]
        total = show[4]
        payment = show[5]

        self.billNoEntry.setText(str(bill))
        self.amountEntry.setText(str(amount))
        self.cgstEntry.setText(str(cgst))
        self.sgstEntry.setText(str(sgst))
        self.finalTotalEntry.setText(str(total))
        self.payEntry.setText(payment)
        try:
            query1 = "SELECT products, hsn, quantity, net_rate, rate, tax, discount, total FROM purchase " \
                     "WHERE supplier_id =? AND date =?"
            ok = cur.execute(query1, (supplierId, date)).fetchall()
        except:
            QMessageBox.information(self,"Information","Unable to load data")

        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)

        for row_data in ok:
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def updateBill(self):
        date = self.dateCombo.currentText()
        billNo = self.billNoEntry.text()
        supplier = self.suppliercombo.text()
        try:
            query = "SELECT products, quantity, net_rate, rate," \
                    "tax, cgst, sgst FROM purchase WHERE supplier = ? AND date =?"
            ok = cur.execute(query,(supplier,date)).fetchall()

            query1 = "SELECT agent, date, payment_mode,supplier," \
                    " amount, total_cgst, " \
                    "total_sgst, total_amount FROM purchase WHERE supplier = ? AND date =?"
            ok1 = cur.execute(query1,(supplier,date)).fetchone()
        except:
            QMessageBox.information(self,"Information","Failed to load data")

        if self.list.selectedItems():
            if self.dateCombo.isEnabled():
                self.update = PurchaseProducts()
                self.update.agentEntry.setText(ok1[0])
                self.update.dateEntry.setDate(QDate.fromString(date, "dd/MM/yyyy"))
                self.update.payCombo.setCurrentText(ok1[2])
                self.update.billNoEntry.setText(str(billNo))
                self.update.supplierCombo.setCurrentText(ok1[3])
                self.update.amountEntry.setText(str(ok1[4]))
                self.update.cgstEntry.setText(str(ok1[5]))
                self.update.sgstEntry.setText(str(ok1[6]))

                for i in reversed(range(self.update.table.rowCount())):
                    self.update.table.removeRow(i)

                for row_data in ok:
                    row_number = self.update.table.rowCount()
                    self.update.table.insertRow(row_number)

                    for column_number, data in enumerate(row_data):
                        self.update.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                        self.update.tableDisplay()
        else:
            QMessageBox.information(self,"Info","Please select a supplier and date to update")

    def deleteBill(self):
        billNo = int(self.billNoEntry.text())
        mbox = QMessageBox.question(self, "Warning", "Are you sure to delete the bill?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                query = "DELETE FROM purchase WHERE billnoId =?"
                cur.execute(query, (billNo,))
                con.commit()

                query1 = "DELETE FROM bills WHERE billnoId =?"
                cur.execute(query1, (billNo,))
                con.commit()
                QMessageBox.information(self, "Information", "Bill has been deleted")

            except:
                QMessageBox.information(self, "Information", "Bill cant be deleted")

            self.billNoEntry.setText("")
            self.suppliercombo.setText("")
            self.payEntry.setText("")
            self.dateCombo.setCurrentText("")
            self.amountEntry.setText("")
            self.cgstEntry.setText("")
            self.sgstEntry.setText("")
            self.finalTotalEntry.setText("")

    def cancel(self):
        self.close()