from PyQt5.QtWidgets import QTableWidgetItem
from Consultas import querys
from Comunicaciones import CNXNSQL

def stockTable(self, results):
    cursor = CNXNSQL.conexion.cursor()
    for row, row_data in enumerate(results):
        self.ui.table_searchItemStock.insertRow(row)
        for col, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            self.ui.table_searchItemStock.setItem(row, col, item)