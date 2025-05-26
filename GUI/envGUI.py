from time import sleep
from PyQt5 import QtWidgets
import sys
import os
from Funciones import insertProducts
##INTERFAZ GRAFICA
from .gui import Ui_MainWindow
from src.core import utils
from src.database import CNXNSQL
from src.models import SearchProduct,UpdateStock


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class envGUI(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(envGUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        cursor = CNXNSQL.conexion.cursor()
        ##navegacion con botones
        self.ui.button_newBill.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.button_searchItems.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.button_updateStock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.button_backBill.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.button_backStock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.button_backSearch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        #numero de factura
        utils.newinvoicenumber(self)

        
        #print(querys.getAllProducts(cursor)[0][0])
        #print(len(querys.getAllProducts(cursor)), "length prfrvetbv")
        
        #Agregar Producto a tabla
        self.ui.button_addProdBill.clicked.connect(lambda: utils.getValuesBills(self))
        #Eliminar producto de tabla
        self.ui.button_deleteProdBill.clicked.connect(lambda: utils.deleteValuesTable(self))
        #Crear factura
        self.ui.button_createBill.clicked.connect(lambda: utils.generarFactura_pdf(self))
        #Search product by Id
        self.ui.button_searchItemStock.clicked.connect(lambda: SearchProduct.searchProductById(self))
        #Get products to create list in Search Product function
        self.ui.button_searchItems.clicked.connect(lambda: SearchProduct.getListProduct(self)) 
        #Clean products table
        self.ui.button_cleanStockTable.clicked.connect(lambda: SearchProduct.getListProduct(self))
        #Insert products in products table
        self.ui.button_addNewItem.clicked.connect(lambda: UpdateStock.insertProductsInProductsTable(self))
                
#ejecucion GUI
if __name__ == '__main__':

    CNXNSQL()
    app = QtWidgets.QApplication(sys.argv)
    GUI = envGUI()
    GUI.show()
    sys.exit(app.exec_())
