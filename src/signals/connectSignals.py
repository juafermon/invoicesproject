
from src.models import SearchProduct,UpdateStock, CreateInvoice

def buttonSignals(self):
    ## Interface navigation ##
    self.ui.button_newBill.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
    self.ui.button_searchItems.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
    self.ui.button_updateStock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
    self.ui.button_backBill.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
    self.ui.button_backStock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
    self.ui.button_backSearch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

    ## Invoice actions ##
    #Add item to bill table button
    self.ui.button_addProdBill.clicked.connect(lambda: CreateInvoice.getItemsAddtoTable(self))
    #Delete item in bill table button
    self.ui.button_deleteProdBill.clicked.connect(lambda: CreateInvoice.deleteProducts(self))
    #Create bill button
    self.ui.button_createBill.clicked.connect(lambda: CreateInvoice.createPDF(self))
    #Search product by Id
    self.ui.button_searchItemStock.clicked.connect(lambda: SearchProduct.searchProductById(self))
    #Get products to create list in Search Product function
    self.ui.button_searchItems.clicked.connect(lambda: SearchProduct.getListProduct(self)) 
    #Clean products table
    self.ui.button_cleanStockTable.clicked.connect(lambda: SearchProduct.getListProduct(self))
    #Insert products in products table
    self.ui.button_addNewItem.clicked.connect(lambda: UpdateStock.insertProductsInProductsTable(self))