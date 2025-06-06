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
    setters.update_quantity(self.ui.input_quantityBill.text())
    setters.update_inv_number(self.ui.label_actualinvnum.text())
    # se agregan las dos funciones de  ValidationsCreateInv porque la forma en la que se
    # estaba haciendo no permite que se valide la entrada de cantidad si no hay idprod, por eso sale el error
    # se puede agregar una bandera para ahi mismo en ValidationsCreateInv 
    ValidationsCreateInv.idProductCamp(self, variables.idProd)
    #ValidationsCreateInv.campQuantity(self, self.ui.input_quantityBill.text())
    self.ui.input_priceBill.setText('') #para borrar el precio, queda pendiente modificar la parte grafica para que no se vea el precio
    
    #SE AGREGAN LAS TRES CONDICIONES, NO ENCONTRE OTRA FORMA DE HACERLO
    if(variables.quantity != '' 
       and variables.price != '' 
       and variables.nameProd != ''):
        self.ui.input_priceBill.setText(str(variables.price)) #Que no se setee el precio antes de entrar al IF
        #Add Items to invoice table
        utils.billTable(self)

def deleteProducts (self):
    actualrows = self.ui.tableBill.rowCount()
    self.ui.tableBill.removeRow(actualrows-1)
    FeaturesCreateInvoice.operTable(self)

def createPDF(self):
    setters.update_inv_date(datetime.now().date())
    FeaturesCreateInvoice.createBill(self)
    
    utils.newBill(self)