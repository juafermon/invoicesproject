from src.database import CNXNSQL, querys
from src.core import variables
from src.services import FeaturesCreateInvoice
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

cursor = CNXNSQL.conexion.cursor()

def newinvoicenumber(self):
    invnum = querys.invoicenumber(CNXNSQL.cursor)
    newinvnum = str(invnum + 1)
    self.ui.label_actualinvnum.setText(newinvnum)

#Function to create a new invoice
def newBill(self):
    self.ui.tableBill.setRowCount(0)
    newinvoicenumber(self)
    self.ui.label_valTotRES.setText("")
    cleanStockTable(self)

def cleanStockTable(self):
    self.ui.table_searchItemStock.setRowCount(0)

def cleanFieldsInsertItem(self):
    self.ui.input_idprodNewItem.setText('')
    self.ui.input_nameNewItem.setText('')
    self.ui.input_priceNewItem.setText('')
    self.ui.input_quantityNewItem.setText('')

#Function to clean fields in invoice
def cleanBillTable(self):
    #Fields reset 
    self.ui.input_idProdBill.setText('')
    self.ui.input_priceBill.setText('')
    self.ui.input_quantityBill.setText('')


def stockTable(self, results):
    for row, row_data in enumerate(results):
        self.ui.table_searchItemStock.insertRow(row)
        for col, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            self.ui.table_searchItemStock.setItem(row, col, item)

#Function that ADD the items in the invoice Table 
def billTable(self):
    Subtotal = str(int(variables.quantity)*int((variables.price)))
    arrayValues = []
    #arrayValues.append(self.ui.input_CCBill.text())
    #arrayValues.append(self.ui.input_nameCLientBill.text())
    #arrayValues.append(self.ui.input_emailBill.text())
    arrayValues.append(variables.idProd)
    arrayValues.append(variables.nameProd)
    #arrayValues.append(querys.productname(cursor, IdProd))
    arrayValues.append(str(variables.price))
    arrayValues.append(variables.quantity)
    arrayValues.append(Subtotal)
    actualrows = self.ui.tableBill.rowCount()
    
    actualStock1 = querys.getProductByID(cursor, variables.idProd)

    diff = actualStock1[0][3]  - int(variables.quantity)
    
    if diff<=0:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"producto {variables.idProd} no disponible")
        msg.setWindowTitle("Advertencia de Valor")
        msg.exec_()

    else:
        self.ui.tableBill.insertRow(actualrows)  
        # FOR loop to add values o the array arrayValues to the bill table 
        for i, value in enumerate (arrayValues):          
            item = QTableWidgetItem(value)
            self.ui.tableBill.setItem(actualrows, i, item)
  
        FeaturesCreateInvoice.operTable(self)

def messageError(self, mensaje):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    aux = f"Producto {mensaje}  no está disponible"
    msg.setText(aux)
    msg.setWindowTitle("Advertencia de Valor")
    msg.exec_()