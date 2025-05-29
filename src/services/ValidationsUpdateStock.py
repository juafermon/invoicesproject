from PyQt5 import QtWidgets

def emptyFields (self, nameProd):
            
        if not nameProd: 
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Debe rellenar al menos un campo para actualizar.")
            msg.setWindowTitle("Advertencia")
            msg.exec_()

def emptyFieldsNewProduct (self, nameProd):
            
        if not nameProd: 
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("El producto no existe, debe rellenar todos los campos para insertarlo.")
            msg.setWindowTitle("Advertencia")
            msg.exec_()