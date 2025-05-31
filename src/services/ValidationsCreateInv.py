from PyQt5 import QtWidgets
from src.core import setters, variables,utils
from src.database import CNXNSQL, querys

#Validations of fields to get products on Bill 
def idProductCamp(self, idProd):
    
    results = querys.getProductByID(CNXNSQL.cursor, idProd)
   
    if not idProd :
        productCamp(self)
    
    elif not results:        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(f"El producto {idProd} no existe, intente de nuevo")  
        msg.setWindowTitle("Advertencia")
        msg.exec_()
        utils.cleanBillTable(self)

    elif not variables.quantity:
        campQuantity(self, variables.quantity)          
    else:
        setters.update_nameProd(results[0][1])  
        setters.update_price(int(results[0][2]))
    
#Field validation idproduct - pop up box 
def productCamp (self):
            
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("El campo Id Producto no puede estar vacío.")
    msg.setWindowTitle("Advertencia")
    msg.exec_()
        
#  Field validation for quantity - pop up box 
def campQuantity (self,Quantity_str):

    try:
        Quantity = int(Quantity_str)
        if Quantity <= 0:

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("El campo cantidad debe ser mayor que 0.")
            msg.setWindowTitle("Advertencia")
            msg.exec_()  

    except :      
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Ingrese un valor valido en el campo cantidad.")
        msg.setWindowTitle("Advertencia")
        msg.exec_() 