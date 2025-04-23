from time import sleep
from PyQt5 import QtWidgets, QtCore
import sys
##para base de datos
from datetime import datetime
##INTERFAZ GRAFICA
from .gui import Ui_MainWindow
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from Comunicaciones import CNXNSQL
from Consultas import querys


class envGUI(QtWidgets.QMainWindow):
    def __init__(self):

        super(envGUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        #botones interfaz
        self.allButtons = {
            "Bill": self.ui.button_createBill,
            "Stock": self.ui.button_updateStock,
            "Backbill": self.ui.button_backBill,
            "BackStock": self.ui.button_backStock,
            "AddProdBill": self.ui.button_addProdBill,
            "DeleteProdBill": self.ui.button_deleteProdBill,
            "CreateBill": self.ui.button_createBill,
            "SearchProd": self.ui.button_searchItemStock,
            "NewItemStock":self.ui.button_createItemStock,
            "UpdateStock": self.ui.button_updateStock_2
        }

        ##navegacion con botones
        self.ui.button_newBill.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.button_updateStock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.button_backBill.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.button_backStock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        #Agregar Producto a tabla
        self.ui.button_addProdBill.clicked.connect(self.getValuesBills)
        #Eliminar producto de tabla
        self.ui.button_deleteProdBill.clicked.connect(self.deleteValuesTable)
        #Crear factura
        self.ui.button_createBill.clicked.connect(self.generarFactura_pdf)
        

    #Obtener valores en Qlineedit seccion Bills y tabla
    def getValuesBills (self):
        cursor = CNXNSQL.conexion.cursor()

        CC = self.ui.input_CCBill.text()
        NameClient = self.ui.input_nameCLientBill.text()
        Email = self.ui.input_emailBill.text()
        IdProd= self.ui.input_idProdBill.text()
        Quantity = self.ui.input_quantityBill.text()
        Price = self.ui.input_priceBill.text()
        NameProd = self.ui.input_nameProdBill.text()

        arrayValues = []
        #arrayValues.append(self.ui.input_CCBill.text())
        #arrayValues.append(self.ui.input_nameCLientBill.text())
        #arrayValues.append(self.ui.input_emailBill.text())
        arrayValues.append(self.ui.input_idProdBill.text())
        arrayValues.append(self.ui.input_nameProdBill.text())
        arrayValues.append(self.ui.input_priceBill.text())
        arrayValues.append(self.ui.input_quantityBill.text())

        actualrows = self.ui.tableBill.rowCount()

        self.ui.tableBill.insertRow(actualrows)
        #if len(CC)>0 and len(Quantity)>0 and len(IdProd)>0 and len(Price)>0:
            #para agregarCNXNSQL() a la tabla
        for i, value in enumerate (arrayValues):
            item = QtWidgets.QTableWidgetItem(value)
            self.ui.tableBill.setItem(actualrows, i, item)

        self.operTable()
        # else:
        #     print("Error de entrada" )

        #agregar a tabla
        # querys.insertquery(cursor, "2", "3")
        # CNXNSQL.conexion.commit()


    #Funcion para eliminar de tabla
    def deleteValuesTable (self):
        actualrows = self.ui.tableBill.rowCount()
        self.ui.tableBill.removeRow(actualrows-1)
        self.operTable()

    def operTable (self):
        col_Prices = 2
        col_Quantity = 3
        columnPrices = []
        columnQuantity = []

        num_rows = self.ui.tableBill.rowCount()
        #precios
        for row in range(num_rows):
            item = self.ui.tableBill.item(row, col_Prices)
            print (self.ui.tableBill.item(row, col_Prices).text(), "ittttem")
            columnPrices.append(item.text())
    
        #cantidad
        for row in range(num_rows):
            item = self.ui.tableBill.item(row, col_Quantity)
            columnQuantity.append(item.text())        

        #multiplicacion
        columnTotal = []
        for i in range(len(columnPrices)):
            total_item = int(''.join(map(str,columnPrices[i]))) * int(''.join(map(str,columnQuantity[i])))
            columnTotal.append(total_item)        
        #Suma Total
        self.ui.label_valTotRES.setText(str(sum(columnTotal)))

    def generarFactura_pdf(self):
        # 1. Recopilacion de datos
        invoice_info = {
            #"numero_factura": self.ui.inputNumberBill.text()
            #"fecha_factura": self.ui.inputDateBill.text(),
            "nombre_cliente": self.ui.input_nameCLientBill.text(),
            "direccion_cliente": self.ui.input_emailBill.text(),
        }
        
        invoice_items = []

        num_rows = self.ui.tableBill.rowCount()
        for row in range(num_rows):
            producto = self.ui.tableBill.item(row, 0).text() if self.ui.tableBill.item(row, 0) else ""
            cantidad = self.ui.tableBill.item(row, 1).text() if self.ui.tableBill.item(row, 1) else ""
            precio_unitario = self.ui.tableBill.item(row, 2).text() if self.ui.tableBill.item(row, 2) else ""
            precio_total = self.ui.tableBill.item(row, 3).text() if self.ui.tableBill.item(row, 3) else ""
            invoice_items.append({
                "producto": producto,
                "cantidad": cantidad,
                "precio_unitario": precio_unitario,
                "precio_total": precio_total
            })

            total_factura = sum(float(item["precio_total"]) for item in invoice_items if item["precio_total"])

                # 2. Renderizar la plantilla HTML con los datos
        env = Environment(loader=FileSystemLoader('.')) # Asume que la plantilla está en el mismo directorio
        template = env.get_template('GUI/invoice/invoice.html')
        html = template.render(
            factura_info=invoice_info,
            items=invoice_items,
            total_factura=total_factura
            )

        # 3. Convertir el HTML a PDF usando xhtml2pdf
        filename = "consecutivo_prueba.pdf"
        with open(filename, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(html, dest=pdf_file)
            if pisa_status.err:
                print(f"Error al generar el PDF: {pisa_status.err}")
            else:
                print(f"Factura generada {filename}")
        

#ejecucion GUI
if __name__ == '__main__':

    CNXNSQL()
    app = QtWidgets.QApplication(sys.argv)
    GUI = envGUI()
    GUI.show()
    sys.exit(app.exec_())
