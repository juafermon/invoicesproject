from PyQt5 import QtWidgets
from Variables import variables
from Funciones import setters
from Comunicaciones import CNXNSQL
from Consultas import querys

#Restricción campo id producto
def campoIdProducto(self, idProd):
    setters.update_nameProd(querys.getProductName(CNXNSQL.cursor, idProd))
    if not idProd :
        campoProducto(self, idProd)
    
    elif variables.nameProd == '' :        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("El producto no existe, intente de nuevo")  
        msg.setWindowTitle("Advertencia")
        msg.exec_()
    elif not variables.quantity:
        campoQuantity(self, variables.quantity)     
    elif  not variables.price:
        campoPrecio(self, variables.price)     
    else:  
        return variables.nameProd
    
    
#Restriccion Campo producto - cuadro de advertencia
def campoProducto (self, IdProd):
            
    
        if not IdProd: 
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("El campo Producto no puede estar vacío.")
            msg.setWindowTitle("Advertencia")
            msg.exec_()
        

#  Restriccion para Quantity - cuadro de advertencia
def campoQuantity (self,Quantity_str):

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
        
def campoPrecio(self, Price_str):
        # --- Restricciones para Price ---
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