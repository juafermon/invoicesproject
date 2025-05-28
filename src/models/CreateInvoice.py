from PyQt5 import QtWidgets
from src.core import setters, variables
from datetime import datetime
from src.services import FeaturesCreateInvoice, ValidationsCreateInv

#Function to get and update the values in the Qlineedit in the bill section
def getValuesBills (self):
    setters.update_cc(self.ui.input_CCBill.text())
    setters.update_nameClient(self.ui.input_nameCLientBill.text())
    setters.update_email(self.ui.input_emailBill.text())
    setters.update_idProd(self.ui.input_idProdBill.text())
    setters.update_quantity(self.ui.input_quantityBill.text().strip())
    setters.update_inv_number(self.ui.label_actualinvnum.text())
    ValidationsCreateInv.idProductCamp(self, variables.idProd)
    self.ui.input_priceBill.setText(str(variables.price))

    if(variables.quantity != '' and variables.price != '' and variables.nameProd != ''):
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
        self.ui.tableBill.insertRow(actualrows)
        # FOR loop to add values o the array arrayValues to the bill table 
        for i, value in enumerate (arrayValues):            
            item = QtWidgets.QTableWidgetItem(value)
            self.ui.tableBill.setItem(actualrows, i, item)
        FeaturesCreateInvoice.operTable(self)

def deleteValuesTable (self):
    actualrows = self.ui.tableBill.rowCount()
    self.ui.tableBill.removeRow(actualrows-1)
    FeaturesCreateInvoice.operTable(self)

def createPDF(self):
    setters.update_inv_date(datetime.now().date())
    FeaturesCreateInvoice.createBill(self)