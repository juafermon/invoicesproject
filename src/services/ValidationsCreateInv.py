from PyQt5 import QtWidgets
from src.core import setters, variables
from src.database import CNXNSQL, querys

#Validations of fields to get products on Bill 
def idProductCamp(self, idProd):
    # 1. Validación de idProd
    if not idProd:
        #revisar como agregar una bandera para que no se activen dos cuadros si no se ingresa producto y no se ingresa cantidad
        # me imagino un 
        # if not idprod:
          #flag
        # else:
          #resto de condiciones
          #productcamp y campquantity
        productCamp(self)
        return
    
    results = querys.getProductByID(CNXNSQL.cursor, idProd)

    # 2. Manejo claro de la ausencia de resultados
    if not results:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("El producto no existe, intente de nuevo")
        msg.setWindowTitle("Advertencia")
        msg.exec_()
        return # Salir si el producto no existe

    # Con este try se asegura que results tenga al menos 3 elementos antes de acceder al array.
    try:
        _, name_prod, price_str = results[0][:3] # Toma los primeros 3 elementos
    except IndexError:
        return

    #Actualizacion de variables globales
    setters.update_nameProd(name_prod)
    setters.update_price(int(price_str))
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