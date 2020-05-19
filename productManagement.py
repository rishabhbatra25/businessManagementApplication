from PyQt5.QtWidgets import *from PyQt5.QtGui import *from PyQt5.QtCore import Qtimport sysimport sqlite3import addProductimport addCustomerimport addSupplierimport Sellproductimport Purchaseproductimport stockimport stylescon = sqlite3.connect("products.db")cur = con.cursor()class Main(QMainWindow):    def __init__(self):        super().__init__()        self.setWindowTitle("Business Management")        self.setGeometry(90, 130, 1800, 800)        #self.setFixedSize(self.size())        self.UI()        self.show()    def UI(self):        self.toolBar()        self.tabWidget()        self.widgets()        self.layout()        self.diplayProduct()        self.diplayCustomer()        self.displaySupplier()    def toolBar(self):        self.tb = self.addToolBar("Tool Bar")        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)        ###################Tool Bar buttons#################        ######################Add Product###################        self.addProduct = QAction(QIcon('icons/add.png'),"Add Product",self)        self.tb.addAction(self.addProduct)        self.addProduct.triggered.connect(self.NewProduct)        self.tb.addSeparator()        ######################Add Customer##################        self.addCustomer = QAction(QIcon('icons/users.png'),"Add Customer",self)        self.tb.addAction(self.addCustomer)        self.addCustomer.triggered.connect(self.NewCustomer)        self.tb.addSeparator()        ######################Add Supplier##################        self.addSupplier = QAction(QIcon('images/images.png'), "Add Supplier", self)        self.addSupplier.triggered.connect(self.NewSupplier)        self.tb.addAction(self.addSupplier)        self.tb.addSeparator()        ##########################Sell Product##################        self.sellProduct = QAction(QIcon('icons/sell.png'),"Sell Product",self)        self.sellProduct.triggered.connect(self.saleBill)        self.tb.addAction(self.sellProduct)        self.tb.addSeparator()        ##########################Purchase Product##################        self.purchaseProduct = QAction(QIcon('img/store.png'), "Purchase Product", self)        self.purchaseProduct.triggered.connect(self.buyingBill)        self.tb.addAction(self.purchaseProduct)        self.tb.addSeparator()        self.viewBill = QAction(QIcon('icons/shop.png'),"View Bill",self)        self.viewBill.triggered.connect(self.billing)        self.tb.addAction(self.viewBill)        self.tb.addSeparator()        self.stock = QAction(QIcon('images/stock.png'),"Stock",self)        self.stock.triggered.connect(self.stocking)        self.tb.addAction(self.stock)        self.tb.addSeparator()    def tabWidget(self):        self.tabs = QTabWidget()        self.setCentralWidget(self.tabs)        self.tab1 = QWidget()        self.tab2 = QWidget()        self.tab3 = QWidget()        self.tabs.addTab(self.tab1,"Products")        self.tabs.addTab(self.tab2,"Customers")        self.tabs.addTab(self.tab3,"Suppliers")    def widgets(self):        self.setStyleSheet("font-size:12pt")        #####################Table Widgets####################        self.productTable = QTableWidget()        self.productTable.setStyleSheet(styles.tableStyle())        self.productTable.setColumnCount(8)        self.productTable.setHorizontalHeaderItem(0,QTableWidgetItem("Product Id"))        self.productTable.setHorizontalHeaderItem(1,QTableWidgetItem("Product Name"))        self.productTable.setHorizontalHeaderItem(2,QTableWidgetItem("Availablity"))        self.productTable.setHorizontalHeaderItem(3,QTableWidgetItem("HSN Code"))        self.productTable.setHorizontalHeaderItem(4,QTableWidgetItem("CGST"))        self.productTable.setHorizontalHeaderItem(5,QTableWidgetItem("SGST"))        self.productTable.setHorizontalHeaderItem(6,QTableWidgetItem("IGST"))        self.productTable.setHorizontalHeaderItem(7,QTableWidgetItem("Under Group"))        self.productTable.doubleClicked.connect(self.selectedProduct)        ###############################search bar widgets###################        self.searchLabel = QLabel("Search")        self.searchEntry = QLineEdit()        self.searchEntry.setPlaceholderText("Search Here")        self.searchBtn = QPushButton("Search")        self.searchBtn.setStyleSheet(styles.buttonStyle2())        self.searchBtn.clicked.connect(self.searchProduct)        ###############################UnderList Widgets###################        self.allProducts = QRadioButton("All Products")        self.availProducts = QRadioButton("Available")        self.notAvailProducts = QRadioButton("Not Available")        self.listBtn = QPushButton("List")        self.listBtn.setStyleSheet(styles.buttonStyle2())        #############################tab2 widgets###########################        self.customerTable = QTableWidget()        self.customerTable.setStyleSheet(styles.tableStyle())        self.customerTable.setColumnCount(10)        self.customerTable.setHorizontalHeaderItem(0, QTableWidgetItem("Customer Id"))        self.customerTable.setHorizontalHeaderItem(1, QTableWidgetItem("Customer Name"))        self.customerTable.setHorizontalHeaderItem(2, QTableWidgetItem("Address"))        self.customerTable.setHorizontalHeaderItem(3, QTableWidgetItem("City"))        self.customerTable.setHorizontalHeaderItem(4, QTableWidgetItem("State"))        self.customerTable.setHorizontalHeaderItem(5, QTableWidgetItem("Phone"))        self.customerTable.setHorizontalHeaderItem(6, QTableWidgetItem("GST NO."))        self.customerTable.setHorizontalHeaderItem(7, QTableWidgetItem("PAN NO."))        self.customerTable.setHorizontalHeaderItem(8, QTableWidgetItem("GST Type"))        self.customerTable.setHorizontalHeaderItem(9, QTableWidgetItem("Under Group"))        self.customerTable.doubleClicked.connect(self.selectedCustomer)        self.customerSearchLabel = QLabel()        self.customerSearchEntry = QLineEdit()        self.customerSearchEntry.setPlaceholderText("Search Here")        self.customerSearchBtn = QPushButton("Search")        self.customerSearchBtn.setStyleSheet(styles.buttonStyle2())        ##################################tab3 widgets###########        self.supplierTable = QTableWidget()        self.supplierTable.setStyleSheet(styles.tableStyle())        self.supplierTable.setColumnCount(10)        self.supplierTable.setHorizontalHeaderItem(0, QTableWidgetItem("Supplier Id"))        self.supplierTable.setHorizontalHeaderItem(1, QTableWidgetItem("Supplier Name"))        self.supplierTable.setHorizontalHeaderItem(2, QTableWidgetItem("Address"))        self.supplierTable.setHorizontalHeaderItem(3, QTableWidgetItem("City"))        self.supplierTable.setHorizontalHeaderItem(4, QTableWidgetItem("State"))        self.supplierTable.setHorizontalHeaderItem(5, QTableWidgetItem("Phone"))        self.supplierTable.setHorizontalHeaderItem(6, QTableWidgetItem("GST NO."))        self.supplierTable.setHorizontalHeaderItem(7, QTableWidgetItem("PAN NO."))        self.supplierTable.setHorizontalHeaderItem(8, QTableWidgetItem("GST Type"))        self.supplierTable.setHorizontalHeaderItem(9, QTableWidgetItem("Under Group"))        self.supplierTable.doubleClicked.connect(self.selectedSupplier)        self.supplierSearchLabel = QLabel()        self.supplierSearchEntry = QLineEdit()        self.supplierSearchEntry.setPlaceholderText("Search Here")        self.supplierSearchBtn = QPushButton("Search")        self.supplierSearchBtn.setStyleSheet(styles.buttonStyle2())    def layout(self):        ########################Tab1 Layouts##############        self.mainLayout = QHBoxLayout()        self.leftLayout = QVBoxLayout()        self.rightMainLayout = QVBoxLayout()        self.rightTopLayout = QHBoxLayout()        self.rightMiddleLayout = QHBoxLayout()        self.rightTopGroupBox = QGroupBox("Search Box")        self.rightMiddleGroupBox = QGroupBox("Listings")        self.rightGroupBox = QGroupBox()        ########################Tab 2 Layouts#####################        self.customerMainLayout = QHBoxLayout()        self.customerLeftLayout = QVBoxLayout()        self.customerRightLayout = QVBoxLayout()        self.CustomerRightGroupBox = QGroupBox("Search")        self.CustomerRightGroupBox.setContentsMargins(10, 20, 10, 600)        ########################Tab 3 Layouts#####################        self.supplierMainLayout = QHBoxLayout()        self.supplierLeftLayout = QVBoxLayout()        self.supplierRightLayout = QVBoxLayout()        self.SupplierRightGroupBox = QGroupBox("Search")        self.SupplierRightGroupBox.setContentsMargins(10, 20, 10, 600)        #########################Adding Widgets##############        self.leftLayout.addWidget(self.productTable)        self.rightTopLayout.addWidget(self.searchLabel)        self.rightTopLayout.addWidget(self.searchEntry)        self.rightTopLayout.addWidget(self.searchBtn)        self.rightMiddleLayout.addWidget(self.allProducts)        self.rightMiddleLayout.addWidget(self.availProducts)        self.rightMiddleLayout.addWidget(self.notAvailProducts)        self.rightMiddleLayout.addWidget(self.listBtn)        self.listBtn.clicked.connect(self.listProducts)        ############################################################        self.customerRightLayout.addWidget(self.customerSearchLabel)        self.customerRightLayout.addWidget(self.customerSearchEntry)        self.customerRightLayout.addWidget(self.customerSearchBtn)        self.customerSearchBtn.clicked.connect(self.searchCustomer)        ############################################################        self.supplierRightLayout.addWidget(self.supplierSearchLabel)        self.supplierRightLayout.addWidget(self.supplierSearchEntry)        self.supplierRightLayout.addWidget(self.supplierSearchBtn)        self.supplierSearchBtn.clicked.connect(self.searchSupplier)        #######################Setting Layouts###############        self.rightTopGroupBox.setLayout(self.rightTopLayout)        self.rightTopGroupBox.setStyleSheet(styles.searchBox())        self.rightMiddleGroupBox.setLayout(self.rightMiddleLayout)        self.mainLayout.addLayout(self.leftLayout,80)        self.rightMainLayout.addWidget(self.rightGroupBox,60)        self.rightMainLayout.addWidget(self.rightTopGroupBox,20)        self.rightMainLayout.addWidget(self.rightMiddleGroupBox,20)        self.rightMiddleGroupBox.setStyleSheet(styles.listBox())        self.mainLayout.addLayout(self.rightMainLayout,20)        self.tab1.setLayout(self.mainLayout)        self.customerLeftLayout.addWidget(self.customerTable)        self.customerMainLayout.addLayout(self.customerLeftLayout,80)        self.CustomerRightGroupBox.setLayout(self.customerRightLayout)        self.CustomerRightGroupBox.setLayout(self.customerRightLayout)        # self.CustomerRightGroupBox.setStyleSheet()        self.customerMainLayout.addWidget(self.CustomerRightGroupBox,20)        self.tab2.setLayout(self.customerMainLayout)        self.supplierLeftLayout.addWidget(self.supplierTable)        self.supplierMainLayout.addLayout(self.supplierLeftLayout, 80)        self.SupplierRightGroupBox.setLayout(self.supplierRightLayout)        self.supplierMainLayout.addWidget(self.SupplierRightGroupBox,20)        self.tab3.setLayout(self.supplierMainLayout)    def NewProduct(self):        self.newProduct = addProduct.AddProduct()        self.close()    def NewCustomer(self):        self.newCustomer = addCustomer.AddCustomer()        self.close()    def NewSupplier(self):        self.newSupplier = addSupplier.AddSupplier()        self.close()    def saleBill(self):        self.sale = Sellproduct.SellProducts()    def billing(self):        self.bill = Sellproduct.viewBills()    def buyingBill(self):        self.buy = Purchaseproduct.PurchaseProducts()    def stocking(self):        self.stokes = stock.Stock()    def diplayProduct(self):        self.productTable.setFont(QFont("candara",12))        for i in reversed(range(self.productTable.rowCount())):            self.productTable.removeRow(i)        query = cur.execute("SELECT * FROM products")        for row_data in query:            row_number = self.productTable.rowCount()            self.productTable.insertRow(row_number)            for column_number, data in enumerate(row_data):                self.productTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))        self.productTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    def diplayCustomer(self):        self.customerTable.setFont(QFont("candara",12))        for i in reversed(range(self.customerTable.rowCount())):            self.customerTable.removeRow(i)        query = cur.execute("SELECT * FROM customers")        for row_data in query:            row_number = self.customerTable.rowCount()            self.customerTable.insertRow(row_number)            for column_number, data in enumerate(row_data):                self.customerTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))        self.customerTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    def displaySupplier(self):        self.supplierTable.setFont(QFont("candara", 12))        for i in reversed(range(self.supplierTable.rowCount())):            self.supplierTable.removeRow(i)        query = cur.execute("SELECT * FROM suppliers")        for row_data in query:            row_number = self.supplierTable.rowCount()            self.supplierTable.insertRow(row_number)            for column_number, data in enumerate(row_data):                self.supplierTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))        self.supplierTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    def selectedProduct(self):        global productId        listProduct = []        for i in range(0,7):            listProduct.append(self.productTable.item(self.productTable.currentRow(),i).text())        productId = listProduct[0]        self.close()        self.product = editProducts()        self.product.show()    def selectedCustomer(self):        global customerId        listCustomer = []        for i in range(0, 8):            listCustomer.append(self.customerTable.item(self.customerTable.currentRow(), i).text())        customerId = listCustomer[0]        self.close()        self.customer = editCustomer()        self.customer.show()    def selectedSupplier(self):        global supplierId        listSupplier = []        for i in range(0, 9):            listSupplier.append(self.supplierTable.item(self.supplierTable.currentRow(), i).text())        supplierId = listSupplier[0]        self.close()        self.supplier = editSupplier()        self.supplier.show()    def searchProduct(self):        value = self.searchEntry.text()        if value =="":            QMessageBox.information(self,"Info","Please enter a name to search")        else:            self.searchEntry.setText("")            query = ("SELECT * FROM products WHERE product_name LIKE ?")            results = cur.execute(query,('%' + value + '%',)).fetchall()                        if results == []:                QMessageBox.information(self,"Info","No products found for this name")            else:                for i in reversed(range(self.productTable.rowCount())):                    self.productTable.removeRow(i)                for row_data in results:                    row_number = self.productTable.rowCount()                    self.productTable.insertRow(row_number)                    for column_number, data in enumerate(row_data):                        self.productTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))    def searchCustomer(self):        value = self.customerSearchEntry.text()        if value =="":            QMessageBox.information(self,"Info","Please enter a name to search")        else:            self.customerSearchEntry.setText("")            query = ("SELECT * FROM customers WHERE customer_name LIKE ?")            results = cur.execute(query,('%' + value + '%',)).fetchall()            if results == []:                QMessageBox.information(self,"Info","No customer found for this name")            else:                for i in reversed(range(self.customerTable.rowCount())):                    self.customerTable.removeRow(i)                for row_data in results:                    row_number = self.customerTable.rowCount()                    self.customerTable.insertRow(row_number)                    for column_number, data in enumerate(row_data):                        self.customerTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))    def searchSupplier(self):        value = self.supplierSearchEntry.text()        if value == "":            QMessageBox.information(self, "Info", "Please enter a name to search")        else:            self.supplierSearchEntry.setText("")            query = ("SELECT * FROM suppliers WHERE supplier_name LIKE ?")            results = cur.execute(query, ('%' + value + '%',)).fetchall()            if results == []:                QMessageBox.information(self, "Info", "No supplier found for this name")            else:                for i in reversed(range(self.supplierTable.rowCount())):                    self.supplierTable.removeRow(i)                for row_data in results:                    row_number = self.supplierTable.rowCount()                    self.supplierTable.insertRow(row_number)                    for column_number, data in enumerate(row_data):                        self.supplierTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))    def listProducts(self):        if self.allProducts.isChecked():            self.diplayProduct()        elif self.availProducts.isChecked():            query = ("SELECT * FROM products WHERE product_availablity = 'Available'")            display = cur.execute(query).fetchall()            for i in reversed(range(self.productTable.rowCount())):                self.productTable.removeRow(i)            for row_data in display:                row_number = self.productTable.rowCount()                self.productTable.insertRow(row_number)                for column_number, data in enumerate(row_data):                    self.productTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))                                elif self.notAvailProducts.isChecked():            query = ("SELECT * FROM products WHERE product_availablity ='Unavailable'")            products = cur.execute(query).fetchall()            for i in reversed(range(self.productTable.rowCount())):                self.productTable.removeRow(i)            for row_data in products:                row_number = self.productTable.rowCount()                self.productTable.insertRow(row_number)                for column_number, data in enumerate(row_data):                    self.productTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))class editCustomer(QWidget):    def __init__(self):        super().__init__()        self.setWindowTitle("Edit Customer Details")        self.setWindowIcon(QIcon('icons/icon.ico'))        self.setGeometry(550, 130, 450, 800)        self.setFixedSize(self.size())        self.UI()        self.show()    def UI(self):        self.customerDetails()        self.layout()        self.widgets()    def customerDetails(self):        global customerId        query = "SELECT * FROM customers WHERE customer_id =?"        customer = cur.execute(query,(customerId,)).fetchone()        self.customerName = customer[1]        self.customerAddress = customer[2]        self.customerCity = customer[3]        self.customerState = customer[4]        self.customerPhone = customer[5]        self.customerGST = customer[6]        self.customerPAN = customer[7]        self.customerGstType = customer[8]        self.customerGroup = customer[9]    def layout(self):        self.mainLayout = QVBoxLayout()        self.topLayout = QVBoxLayout()        self.bottomLayout = QFormLayout()        self.topFrame = QFrame()        self.bottomFrame = QFrame()        ########################################################        self.topFrame.setLayout(self.topLayout)        self.bottomFrame.setLayout(self.bottomLayout)    def widgets(self):        self.title = QLabel("Update Customer")        self.title.setAlignment(Qt.AlignCenter)        self.imgAdd = QLabel()        self.imgAdd.setPixmap(QPixmap("icons/members.png"))        self.imgAdd.setAlignment(Qt.AlignCenter)        #####################bottom layout############        self.nameLabel = QLabel("Name :")        self.nameEntry = QLineEdit()        self.nameEntry.setText(self.customerName)        self.addressLabel = QLabel("Address :")        self.addressEntry = QLineEdit()        self.addressEntry.setText(self.customerAddress)        self.cityLabel = QLabel("City :")        self.cityEntry = QLineEdit()        self.cityEntry.setText(self.customerCity)        self.stateLabel = QLabel("State :")        self.stateEntry = QLineEdit()        self.stateEntry.setText(self.customerState)        self.phoneLabel = QLabel("Phone :")        self.phoneEntry = QLineEdit()        self.phoneEntry.setText(self.customerPhone)        self.gstLabel = QLabel("GST No :")        self.gstEntry = QLineEdit()        self.gstEntry.setText(self.customerGST)        self.panLabel = QLabel("PAN No :")        self.panEntry = QLineEdit()        self.panEntry.setText(self.customerPAN)        self.gstTypeCombo = QComboBox()        self.gstTypeCombo.addItems(["Unregistered", "Regular","Composition"])        self.customerGroupCombo = QComboBox()        self.deleteBtn = QPushButton("Delete")        self.deleteBtn.clicked.connect(self.deleteCustomer)        self.updateBtn = QPushButton("Update")        self.updateBtn.clicked.connect(self.updateCustomer)        self.underGroupLabel = QLabel("Under Group :")        self.underGroup = QComboBox()        self.underGroup.addItem("Commission A/C")        self.underGroup.addItem("Assets A/C")        self.underGroup.addItem("Bank A/C")        self.underGroup.addItem("Cash in Hand A/C")        self.underGroup.addItem("Capital A/C")        self.underGroup.addItem("Defaulter A/C")        self.underGroup.addItem("Delivery A/C")        self.underGroup.addItem("Supplier A/C")        self.underGroup.addItem("Expenses")        self.underGroup.addItem("Investment")        self.underGroup.addItem("Loan and Advance")        self.underGroup.addItem("Opening Stock")        self.underGroup.addItem("Sales A/C")        self.underGroup.addItem("Purchase Expenses")        self.underGroup.addItem("Sales Promotion")        self.underGroup.addItem("Sallary Advance")        self.underGroup.addItem("Duties and Taxes")        self.underGroup.addItem("Secured Loan A/C")        self.underGroup.addItem("Supplier A/C")        self.underGroup.addItem("Credit A/C")        self.underGroup.addItem("Unsecured Loans")        self.topLayout.addWidget(self.title)        self.topLayout.addWidget(self.imgAdd)        ##################################################333333        self.bottomLayout.addRow(self.nameLabel,self.nameEntry)        self.bottomLayout.addRow(self.addressLabel,self.addressEntry)        self.bottomLayout.addRow(self.cityLabel,self.cityEntry)        self.bottomLayout.addRow(self.stateLabel,self.stateEntry)        self.bottomLayout.addRow(self.phoneLabel,self.phoneEntry)        self.bottomLayout.addRow(self.gstLabel,self.gstEntry)        self.bottomLayout.addRow(self.panLabel,self.panEntry)        self.bottomLayout.addRow(QLabel("GST Type :"),self.gstTypeCombo)        self.bottomLayout.addRow(QLabel("Under Group :"),self.underGroup)        self.bottomLayout.addRow("",self.deleteBtn)        self.bottomLayout.addRow("",self.updateBtn)        self.mainLayout.addWidget(self.topFrame)        self.mainLayout.addWidget(self.bottomFrame)        self.setLayout(self.mainLayout)    def deleteCustomer(self):        global customerId        mbox = QMessageBox.question(self,"Warning","Are you sure to delete the Customer",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)        if mbox ==QMessageBox.Yes:            try:                query = "DELETE FROM customers WHERE customer_id =?"                cur.execute(query,(customerId,))                con.commit()                QMessageBox.information(self,"Information","Customer has been deleted")                self.close()                self.open = Main()                self.open.show()            except:                QMessageBox.information(self,"Information","Customer cant be deleted")    def updateCustomer(self):        global customerId        self.name = self.nameEntry.text()        self.address = self.addressEntry.text()        self.city = self.cityEntry.text()        self.state = self.stateEntry.text()        self.phone = self.phoneEntry.text()        self.gst = self.gstEntry.text()        self.pan = self.panEntry.text()        self.gstType = self.gstTypeCombo.currentText()        self.group = self.customerGroupCombo.currentText()        if (self.name !=""):            try:                query = "UPDATE customers SET customer_name =?,customer_address =?,customer_city =?,customer_state =?,customer_mobile =?,customer_gst =?,customer_pan =?, customer_gst_type =?,customer_group =? WHERE customer_id =?"                cur.execute(query,(self.name,self.address,self.city,self.state,self.phone,self.gst,self.pan,self.gstType,self.group,customerId))                con.commit()                QMessageBox.information(self,"Information","Customer details updated")                self.close()                self.open = Main()                self.open.show()            except:                QMessageBox.information(self,"Information","Customer details not updated")        else:            QMessageBox.information(self,"Information","Please Enter Name")class editProducts(QWidget):    def __init__(self):        super().__init__()        self.setWindowTitle("Edit Products")        self.setWindowIcon(QIcon('icons/icon.ico'))        self.setGeometry(550, 130, 450, 800)        self.setFixedSize(self.size())        self.UI()        self.show()    def UI(self):        self.productDetails()        self.widgets()        self.layout()    def productDetails(self):        global productId        query = ("SELECT * FROM products WHERE product_id = ?")        product = cur.execute(query,(productId,)).fetchone()        self.productName = product[1]        self.productHSN = product[3]        self.productCGST = product[4]        self.productSGST = product[5]        self.productIGST = product[6]        self.productGroup = product[7]    def widgets(self):        self.title = QLabel("Update Product")        self.imgAdd = QLabel()        self.imgAdd.setPixmap(QPixmap("images/images.png"))        self.imgAdd.setAlignment(Qt.AlignCenter)        #####################bottom layout############        self.nameLabel = QLabel("Name :")        self.nameEntry = QLineEdit()        self.nameEntry.setText(self.productName)        self.hsnLabel = QLabel("HSN Code :")        self.hsnEntry = QLineEdit()        self.hsnEntry.setText(self.productHSN)        self.cgstLabel = QLabel("CGST :")        self.cgstEntry = QLineEdit()        self.cgstEntry.setText(str(self.productCGST))        self.sgstLabel = QLabel("SGST :")        self.sgstEntry = QLineEdit()        self.sgstEntry.setText(str(self.productSGST))        self.igstLabel = QLabel("IGST :")        self.igstEntry = QLineEdit()        self.igstEntry.setText(str(self.productIGST))        self.availableLabel = QLabel("Availablity :")        self.availableCombo = QComboBox()        self.availableCombo.addItems(["Available", "Unavailable"])        self.deleteBtn = QPushButton("Delete")        self.deleteBtn.clicked.connect(self.deleteProduct)        self.updateBtn = QPushButton("Update")        self.updateBtn.clicked.connect(self.updateProduct)        self.underGroupLabel = QLabel("Under Group :")        self.underGroupCombo = QComboBox()        self.underGroupCombo.addItem("Tax Free")        self.underGroupCombo.addItem("3%")        self.underGroupCombo.addItem("5%")        self.underGroupCombo.addItem("12%")        self.underGroupCombo.addItem("18%")        self.underGroupCombo.addItem("28%")    def layout(self):        self.mainLayout = QVBoxLayout()        self.topLayout = QVBoxLayout()        self.bottomLayout = QFormLayout()        self.topFrame = QFrame()        self.bottomFrame = QFrame()        ########################################################        self.topFrame.setLayout(self.topLayout)        self.bottomFrame.setLayout(self.bottomLayout)        #######################################3#############        self.topLayout.addWidget(self.title)        self.topLayout.addWidget(self.imgAdd)        ######################################################        self.bottomLayout.addRow(self.nameLabel, self.nameEntry)        self.bottomLayout.addRow(self.hsnLabel, self.hsnEntry)        self.bottomLayout.addRow(self.cgstLabel, self.cgstEntry)        self.bottomLayout.addRow(self.sgstLabel, self.sgstEntry)        self.bottomLayout.addRow(self.igstLabel, self.igstEntry)        self.bottomLayout.addRow(self.availableLabel, self.availableCombo)        self.bottomLayout.addRow(self.underGroupLabel, self.underGroupCombo)        self.bottomLayout.addRow("", self.deleteBtn)        self.bottomLayout.addRow("", self.updateBtn)        self.mainLayout.addWidget(self.topFrame)        self.mainLayout.addWidget(self.bottomFrame)        self.setLayout(self.mainLayout)        ##########################################################    def updateProduct(self):        global productId        self.name = self.nameEntry.text()        self.status = self.availableCombo.currentText()        self.hsn = self.hsnEntry.text()        self.cgst = self.cgstEntry.text()        self.sgst = self.sgstEntry.text()        self.igst = self.igstEntry.text()        self.group = self.underGroupCombo.currentText()        if (self.name !=""):            try:                query ="UPDATE products set product_name= ?,product_availablity= ?,product_hsn= ?,product_cgst= ?,product_sgst= ?,product_igst= ?,product_group= ? WHERE product_id= ?"                cur.execute(query, (self.name, self.status, self.hsn, self.cgst,self.sgst,self.igst,self.group,productId))                con.commit()                QMessageBox.information(self, "Information", "Product has been updated")                self.close()                self.open = Main()                self.open.show()            except:                QMessageBox.information(self, "Information", "Product has not been updated")        else:            QMessageBox.information(self, "Information", "Please enter name")    def deleteProduct(self):        global productId        mbox = QMessageBox.question(self,"Warning","Are you sure to delete the product",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)        if mbox ==QMessageBox.Yes:            try:                query = "DELETE FROM products WHERE product_id =?"                cur.execute(query,(productId,))                con.commit()                QMessageBox.information(self,"Information","Product has been deleted")                self.close()                self.open = Main()                self.open.show()            except:                QMessageBox.information(self,"Information","Product cant be deleted")class editSupplier(QWidget):    def __init__(self):        super().__init__()        self.setWindowTitle("Edit Supplier Details")        self.setWindowIcon(QIcon('icons/icon.ico'))        self.setGeometry(550, 130, 450, 800)        self.setFixedSize(self.size())        self.UI()        self.show()    def UI(self):        self.supplierDetails()        self.layout()        self.widgets()    def supplierDetails(self):        global supplierId        query = "SELECT * FROM suppliers WHERE supplier_id =?"        supplier = cur.execute(query,(supplierId,)).fetchone()        self.supplierName = supplier[1]        self.supplierAddress = supplier[2]        self.supplierCity = supplier[3]        self.supplierState = supplier[4]        self.supplierPhone = supplier[5]        self.supplierGST = supplier[6]        self.supplierPAN = supplier[7]        self.supplierGstType = supplier[8]        self.supplierGroup = supplier[9]    def layout(self):        self.mainLayout = QVBoxLayout()        self.topLayout = QVBoxLayout()        self.bottomLayout = QFormLayout()        self.topFrame = QFrame()        self.bottomFrame = QFrame()        ########################################################        self.topFrame.setLayout(self.topLayout)        self.bottomFrame.setLayout(self.bottomLayout)    def widgets(self):        self.title = QLabel("Update supplier")        self.title.setAlignment(Qt.AlignCenter)        # self.title.setStyleSheet("font-family:tahoma Bold;font-size:22pt")        self.imgAdd = QLabel()        self.imgAdd.setPixmap(QPixmap("icons/members.png"))        self.imgAdd.setAlignment(Qt.AlignCenter)        #####################bottom layout############        self.nameLabel = QLabel("Name :")        self.nameEntry = QLineEdit()        self.nameEntry.setText(self.supplierName)        self.addressLabel = QLabel("Address :")        self.addressEntry = QLineEdit()        self.addressEntry.setText(self.supplierAddress)        self.cityLabel = QLabel("City :")        self.cityEntry = QLineEdit()        self.cityEntry.setText(self.supplierCity)        self.stateLabel = QLabel("State :")        self.stateEntry = QLineEdit()        self.stateEntry.setText(self.supplierState)        self.phoneLabel = QLabel("Phone :")        self.phoneEntry = QLineEdit()        self.phoneEntry.setText(self.supplierPhone)        self.gstLabel = QLabel("GST No :")        self.gstEntry = QLineEdit()        self.gstEntry.setText(self.supplierGST)        self.panLabel = QLabel("PAN No :")        self.panEntry = QLineEdit()        self.panEntry.setText(self.supplierPAN)        self.gstTypeCombo = QComboBox()        self.gstTypeCombo.addItems(["Unregistered", "Regular","Composition"])        self.supplierGroupCombo = QComboBox()        self.deleteBtn = QPushButton("Delete")        self.deleteBtn.clicked.connect(self.deleteSupplier)        self.updateBtn = QPushButton("Update")        self.updateBtn.clicked.connect(self.updateSupplier)        self.underGroupLabel = QLabel("Under Group :")        self.underGroup = QComboBox()        self.underGroup.addItem("Commission A/C")        self.underGroup.addItem("Assets A/C")        self.underGroup.addItem("Bank A/C")        self.underGroup.addItem("Cash in Hand A/C")        self.underGroup.addItem("Capital A/C")        self.underGroup.addItem("Defaulter A/C")        self.underGroup.addItem("Delivery A/C")        self.underGroup.addItem("Supplier A/C")        self.underGroup.addItem("Expenses")        self.underGroup.addItem("Investment")        self.underGroup.addItem("Loan and Advance")        self.underGroup.addItem("Opening Stock")        self.underGroup.addItem("Sales A/C")        self.underGroup.addItem("Purchase Expenses")        self.underGroup.addItem("Sales Promotion")        self.underGroup.addItem("Sallary Advance")        self.underGroup.addItem("Duties and Taxes")        self.underGroup.addItem("Secured Loan A/C")        self.underGroup.addItem("Supplier A/C")        self.underGroup.addItem("Credit A/C")        self.underGroup.addItem("Unsecured Loans")        self.topLayout.addWidget(self.title)        self.topLayout.addWidget(self.imgAdd)        ##################################################333333        self.bottomLayout.addRow(self.nameLabel,self.nameEntry)        self.bottomLayout.addRow(self.addressLabel,self.addressEntry)        self.bottomLayout.addRow(self.cityLabel,self.cityEntry)        self.bottomLayout.addRow(self.stateLabel,self.stateEntry)        self.bottomLayout.addRow(self.phoneLabel,self.phoneEntry)        self.bottomLayout.addRow(self.gstLabel,self.gstEntry)        self.bottomLayout.addRow(self.panLabel,self.panEntry)        self.bottomLayout.addRow(QLabel("GST Type :"),self.gstTypeCombo)        self.bottomLayout.addRow(QLabel("Under Group :"),self.underGroup)        self.bottomLayout.addRow("",self.deleteBtn)        self.bottomLayout.addRow("",self.updateBtn)        self.mainLayout.addWidget(self.topFrame)        self.mainLayout.addWidget(self.bottomFrame)        self.setLayout(self.mainLayout)    def deleteSupplier(self):        global supplierId        mbox = QMessageBox.question(self,"Warning","Are you sure to delete the supplier",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)        if mbox ==QMessageBox.Yes:            try:                query = "DELETE FROM suppliers WHERE supplier_id =?"                cur.execute(query,(supplierId,))                con.commit()                QMessageBox.information(self,"Information","supplier has been deleted")                self.close()                self.open = Main()                self.open.show()            except:                QMessageBox.information(self,"Information","supplier cant be deleted")    def updateSupplier(self):        global supplierId        self.name = self.nameEntry.text()        self.address = self.addressEntry.text()        self.city = self.cityEntry.text()        self.state = self.stateEntry.text()        self.phone = self.phoneEntry.text()        self.gst = self.gstEntry.text()        self.pan = self.panEntry.text()        self.gstType = self.gstTypeCombo.currentText()        self.group = self.supplierGroupCombo.currentText()        if (self.name !=""):            try:                query = "UPDATE suppliers SET supplier_name =?,supplier_address =?,supplier_city =?,supplier_state =?," \                        "supplier_mobile =?,supplier_gst =?,supplier_pan =?, supplier_gst_type =?,supplier_group =? " \                        "WHERE supplier_id =?"                cur.execute(query,(self.name,self.address,self.city,self.state,self.phone,self.gst,self.pan,self.gstType,self.group,supplierId))                con.commit()                QMessageBox.information(self,"Information","supplier details updated")                self.close()                self.open = Main()                self.open.show()            except:                QMessageBox.information(self,"Information","supplier details not updated")        else:            QMessageBox.information(self,"Information","Please Enter Name")def main():    App = QApplication(sys.argv)    window = Main()    sys.exit(App.exec_())if __name__ == '__main__':    main()