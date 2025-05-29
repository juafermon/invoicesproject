from PyQt5 import QtWidgets
from src.core import setters, variables
from src.database import CNXNSQL, querys

#Validations of fields to get products on Bill 
def idProductCamp(self, idProd):
    results = querys.getProductByID(CNXNSQL.cursor, idProd)

    setters.update_nameProd(results[0][1])
    setters.update_price(int(results[0][2]))

    if not idProd :
        productCamp(self, idProd)
    
    elif variables.nameProd == '' :        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("El producto no existe, intente de nuevo")  
        msg.setWindowTitle("Advertencia")
        msg.exec_()
    elif not variables.quantity:
        campQuantity(self, variables.quantity)     
    elif  not variables.price:
        campPrice(self, variables.price)     
    else:  
        return variables.nameProd
    
    
#Field validation idproduct - pop up box 
def productCamp (self, IdProd):
            
        if not IdProd: 
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("El campo Id Producto no puede estar vacío.")
            msg.setWindowTitle("Advertencia")
            msg.exec_()
        
#  Field validation for quantity - pop up box 
def campQuantity (self,Quantity_str):

        if not Quantity_str:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("El campo Cantidad no puede estar vacío.")
            msg.setWindowTitle("Advertencia")
            msg.exec_()  
            return

        try:
            Quantity = int(Quantity_str)
            if Quantity <= 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("El campo Cantidad debe ser positivo.")
                msg.setWindowTitle("Advertencia")
                msg.exec_()  
                return
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Ingrese un valor valido en cantidad")
            msg.setWindowTitle("Advertencia")
            msg.exec_()  
            return
        

# --- Field validation for Price ---
def campPrice(self, Price_str):

        if not Price_str:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Campo precio no puede estar vacio")
            msg.setWindowTitle("Advertencia")
            msg.exec_()  
            return

        try:
            if int(Price_str) <= 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Campo precio debe ser positivo")
                msg.setWindowTitle("Advertencia")
                msg.exec_() 
                returnPrice = float(Price_str) # Intentamos convertir a float para permitir decimales
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Campo precio invalido")
            msg.setWindowTitle("Advertencia")
            msg.exec_() 
            return