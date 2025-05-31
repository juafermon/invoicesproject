from PyQt5 import QtWidgets
from src.core import setters, variables, utils
from datetime import datetime
from src.services import FeaturesCreateInvoice, ValidationsCreateInv

#Function to get and update the values in the Qlineedit in the bill section
def getItemsAddtoTable (self):
    setters.update_cc(self.ui.input_CCBill.text())
    setters.update_nameClient(self.ui.input_nameCLientBill.text())
    setters.update_email(self.ui.input_emailBill.text())
    setters.update_idProd(self.ui.input_idProdBill.text())
    setters.update_quantity(self.ui.input_quantityBill.text().strip())
    setters.update_inv_number(self.ui.label_actualinvnum.text())
    ValidationsCreateInv.idProductCamp(self, variables.idProd)
    self.ui.input_priceBill.setText(str(variables.price))

    if(variables.quantity != '' and variables.nameProd != ''):
        #Add Items to invoice table
        utils.billTable(self)

def deleteProducts (self):
    actualrows = self.ui.tableBill.rowCount()
    self.ui.tableBill.removeRow(actualrows-1)
    FeaturesCreateInvoice.operTable(self)

def createPDF(self):
    setters.update_inv_date(datetime.now().date())
    #FeaturesCreateInvoice.updateStockAfterCreateBill(self)
    FeaturesCreateInvoice.createBill(self)
    
    utils.newBill(self)