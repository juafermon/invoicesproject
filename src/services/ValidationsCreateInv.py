from PyQt5 import QtWidgets
from src.core import setters, variables
from src.database import CNXNSQL, querys

#Validations of fields to get products on Bill 
def idProductCamp(self, idProd):
    # 1. Validación de idProd
    if not idProd:
        productCamp(self)
        return
    else:
        results = querys.getProductByID(CNXNSQL.cursor, idProd)

        # Manejo claro de la ausencia de resultados
        if not results:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(f"El producto {idProd} no existe, intente de nuevo")
            msg.setWindowTitle("Advertencia")
            msg.exec_()
            return # Salir si el producto no existe
        
        else:
            campQuantity(self, variables.quantity)

        # Con este try se asegura que results tenga al menos 3 elementos antes de acceder al array.
        #Actualizacion de variables globales
        setters.update_nameProd(results[0][1])
        setters.update_price(int(results[0][2]))
        return variables.nameProd
    
    
#Field validation idproduct - pop up box 
def productCamp (self):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(f"El campo Id Producto no puede estar vacío.")
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
        #variable global asignada
        variables.quantity = Quantity
        return # La validación fue exitosa

    except ValueError:
        # Field validation for quantity - pop up box
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Ingrese solo números en el campo de cantidad.")
        msg.setWindowTitle("Advertencia")
        msg.exec_()
        #variable global asignada
        variables.quantity = ''
        return