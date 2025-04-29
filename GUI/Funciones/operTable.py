import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def operTable (self):
    col_SubTotal = 4  
    arraySubTotal = []  

    num_rows = self.ui.tableBill.rowCount()
    #array subtotal
    for row in range(num_rows):
        item = self.ui.tableBill.item(row, col_SubTotal)
        arraySubTotal.append(item.text())     

    #SumSubtotal
    convertedarray= []
    for i in range(len(arraySubTotal)):
        totalItem = int(''.join(map(str,arraySubTotal[i])))
        convertedarray.append(totalItem)

    #Suma Total
    self.ui.label_valTotRES.setText(str(sum(convertedarray)))