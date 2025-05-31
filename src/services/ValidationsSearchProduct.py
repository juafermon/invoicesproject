from PyQt5 import QtWidgets
from src.services import ValidationsCreateInv

def searchIdField(self, idProd):
     
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(f"El producto {idProd} no existe, intente de nuevo")  
        msg.setWindowTitle("Advertencia")
        msg.exec_()