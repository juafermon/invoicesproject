from src.database import CNXNSQL, querys
from src.core import variables, setters, utils
from src.services import ValidationsCreateInv
from src.services import FeaturesCreateInvoice
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

cursor = CNXNSQL.conexion.cursor()

def newinvoicenumber(self):
    invnum = querys.invoicenumber(CNXNSQL.cursor)
    
    #Control when there are not exits any invoice
    if not invnum:
        newinvnum = 1
    else: 
        newinvnum = str(invnum + 1)
    
    self.ui.label_actualinvnum.setText(str(newinvnum))

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
    self.ui.input_quantityBill.setText('')


def stockTable(self, results):
    #Modify values in results variable to add $ symbol and separator (.)
    temporal = []
    for i,element in enumerate(results):  
        fila = (
            str(results[i][0]), 
            str(results[i][1]), 
            str('$ ' + utils.formatNumber(self, int(element[2]))), 
            str(results[i][3])
            )
        temporal.append(fila)
    results2 = tuple(temporal)
    
    for row, row_data in enumerate(results2): 
        self.ui.table_searchItemStock.insertRow(row)
        for col, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            self.ui.table_searchItemStock.setItem(row, col, item)
            

#Function that ADD the items in the invoice Table 
def billTable(self):
    Subtotal= str(int(variables.quantity)*int((variables.price)))
    arrayValues = []
    #arrayValues.append(self.ui.input_CCBill.text())
    #arrayValues.append(self.ui.input_nameCLientBill.text())
    #arrayValues.append(self.ui.input_emailBill.text())
    arrayValues.append(variables.idProd)
    arrayValues.append(variables.nameProd)
    #arrayValues.append(querys.productname(cursor, IdProd))
    arrayValues.append(str(variables.quantity))
    arrayValues.append('$ ' + utils.formatNumber(self, variables.price))
    arrayValues.append('$ ' + utils.formatNumber(self, int(Subtotal)))
    actualrows = self.ui.tableBill.rowCount()
    
    actualStock = querys.getProductByID(cursor, variables.idProd)
    
    diff = actualStock[0][3]  - int(variables.quantity)

    if diff<0:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"Existencias insuficientes, la cantidad existente para el producto {variables.idProd} es de {actualStock[0][3]} unidades.")
        msg.setWindowTitle("Advertencia de Valor")
        msg.exec_()
                
    else:

        for i in range (actualrows):
            item = self.ui.tableBill.item(i,0)
            if item.text() == variables.idProd:
                ValidationsCreateInv.existingItemBillTable(self, variables.idProd)
                return

        setters.update_quantity('')
        setters.update_nameProd('')
        self.ui.tableBill.insertRow(actualrows)  
        # FOR loop to add values o the array arrayValues to the bill table 
        for i, value in enumerate (arrayValues):          
            item = QTableWidgetItem(value)
            self.ui.tableBill.setItem(actualrows, i, item)

        FeaturesCreateInvoice.operTable(self)

def formatNumber(self, number):
    newNumber = f'{number:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return newNumber

def eraseFormatNumber(self, number):
    newNumberWithoutFormat = number.replace('$ ', '').replace('.', '').replace(',00','')
    return newNumberWithoutFormat
