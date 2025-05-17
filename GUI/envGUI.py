from time import sleep
from PyQt5 import QtWidgets, QtCore
import sys
import os
from datetime import datetime
##INTERFAZ GRAFICA
from .gui import Ui_MainWindow
from Comunicaciones import CNXNSQL
from Consultas import querys
from Funciones import utils, restricciones,calculos
from Variables import variables


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
        
        #Agregar Producto a tabla
        self.ui.button_addProdBill.clicked.connect(lambda: utils.getValuesBills(self))
        #Eliminar producto de tabla
        self.ui.button_deleteProdBill.clicked.connect(lambda: utils.deleteValuesTable(self))
        #Crear factura
        self.ui.button_createBill.clicked.connect(lambda: utils.generarFactura_pdf(self))
        #Buscar producto en pantalla de inventario
        self.ui.button_searchItemStock.clicked.connect(lambda: utils.buscarProductoEnInventarioPorId(self))
        
#ejecucion GUI
if __name__ == '__main__':

    CNXNSQL()
    app = QtWidgets.QApplication(sys.argv)
    GUI = envGUI()
    GUI.show()
    sys.exit(app.exec_())
