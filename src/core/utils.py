# from jinja2 import Environment, FileSystemLoader
# from xhtml2pdf import pisa
# from Funciones import restricciones, calculos
# from src.core import variables, setters
# from PyQt5 import QtWidgets
# from datetime import datetime
from src.database import CNXNSQL, querys
from PyQt5.QtWidgets import QTableWidgetItem

cursor = CNXNSQL.conexion.cursor()

def newinvoicenumber(self):
    invnum = querys.invoicenumber(CNXNSQL.cursor)
    newinvnum = str(invnum + 1)
    self.ui.label_actualinvnum.setText(newinvnum)

def cleanStockTable(self):
    self.ui.table_searchItemStock.setRowCount(0)


def cleanFieldsInsertItem(self):
    self.ui.input_idprodNewItem.setText('')
    self.ui.input_nameNewItem.setText('')
    self.ui.input_priceNewItem.setText('')
    self.ui.input_quantityNewItem.setText('')


def stockTable(self, results):

    for row, row_data in enumerate(results):
        self.ui.table_searchItemStock.insertRow(row)
        for col, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            self.ui.table_searchItemStock.setItem(row, col, item)