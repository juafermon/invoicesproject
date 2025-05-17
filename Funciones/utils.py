
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from Funciones import restricciones, setters, calculos
from Variables import variables
from PyQt5 import QtWidgets
from Consultas import querys
from Comunicaciones import CNXNSQL
from datetime import datetime
from Funciones import printStockTable


def newinvoicenumber(self):
    invnum = querys.invoicenumber(CNXNSQL.cursor)
    newinvnum = str(invnum + 1)
    self.ui.label_actualinvnum.setText(newinvnum)
    

    #Obtener valores en Qlineedit seccion Bills y tabla
def getValuesBills (self):
    
    setters.update_cc(self.ui.input_CCBill.text())
    setters.update_nameClient(self.ui.input_nameCLientBill.text())
    setters.update_email(self.ui.input_emailBill.text())
    setters.update_idProd(self.ui.input_idProdBill.text())
    setters.update_quantity(self.ui.input_quantityBill.text().strip())
    setters.update_price(self.ui.input_priceBill.text())
    setters.update_inv_number(self.ui.label_actualinvnum.text())
    restricciones.campoIdProducto(self, variables.idProd)

    #setters.update_nameProd = self.ui.input_nameProdBill.text()
    if(variables.quantity != '' and variables.price != '' and variables.nameProd != ''):
            Subtotal = str(int(variables.quantity)*int(variables.price))

            arrayValues = []
            #arrayValues.append(self.ui.input_CCBill.text())
            #arrayValues.append(self.ui.input_nameCLientBill.text())
            #arrayValues.append(self.ui.input_emailBill.text())
            arrayValues.append(variables.idProd)
            arrayValues.append(variables.nameProd)
            #arrayValues.append(querys.productname(cursor, IdProd))
            arrayValues.append(variables.price)
            arrayValues.append(variables.quantity)
            arrayValues.append(Subtotal)
            
            actualrows = self.ui.tableBill.rowCount()
            self.ui.tableBill.insertRow(actualrows)
            # For para agregar valores de arrayValues a tabla
            for i, value in enumerate (arrayValues):
                item = QtWidgets.QTableWidgetItem(value)
                self.ui.tableBill.setItem(actualrows, i, item)
            
            #
            calculos.operTable(self)

#Funcion para eliminar items de tabla
def deleteValuesTable (self):
    actualrows = self.ui.tableBill.rowCount()
    self.ui.tableBill.removeRow(actualrows-1)
    calculos.operTable(self)

#Funcion para crear facturas
def generarFactura_pdf(self):
    cursor = CNXNSQL.conexion.cursor()
    setters.update_inv_date(datetime.now().date())
    #today = datetime.now()
    # 1. Recopilacion de datos
    invoice_info = {
        "numero_factura": variables.invoice_num,
        "fecha_factura": variables.invoice_date.strftime("%Y %m %d"),
        "nombre_cliente": variables.nameClient,
        "direccion_cliente": variables.email,
    }
    
    invoice_items = []

    num_rows = self.ui.tableBill.rowCount()
    for row in range(num_rows):
        id_producto = self.ui.tableBill.item(row, 0).text() if self.ui.tableBill.item(row, 0) else ""
        producto = self.ui.tableBill.item(row, 1).text() if self.ui.tableBill.item(row, 1) else ""
        cantidad = self.ui.tableBill.item(row, 2).text() if self.ui.tableBill.item(row, 2) else ""
        precio_unitario = self.ui.tableBill.item(row, 3).text() if self.ui.tableBill.item(row, 3) else ""
        precio_total = self.ui.tableBill.item(row, 4).text() if self.ui.tableBill.item(row, 4) else ""
        invoice_items.append({
            "id_producto": id_producto,
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "precio_total": precio_total,
        })

        
        total_factura = sum(float(item["precio_total"]) for item in invoice_items if item["precio_total"])
        
        querys.insertInfoInvoiceTable(cursor,id_producto, cantidad,precio_total,total_factura,variables.invoice_date,variables.invoice_num)
        CNXNSQL.conexion.commit()

            # 2. Renderizar la plantilla HTML con los datos
    env = Environment(loader=FileSystemLoader('.')) # Asume que la plantilla está en el mismo directorio
    template = env.get_template('GUI/invoice/invoice.html')
    html = template.render(
        factura_info=invoice_info,
        items=invoice_items,
        total_factura=total_factura
        )

    # 3. Convertir el HTML a PDF usando xhtml2pdf
    filename = f"{variables.invoice_num}{variables.invoice_date.strftime("%Y %m %d").replace(" ","")}.pdf"
    with open(filename, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html, dest=pdf_file)
        if pisa_status.err:
            print(f"Error al generar el PDF: {pisa_status.err}")
        else:
            print(f"Factura generada {filename}")

    #reset de los campos
    self.ui.input_idProdBill.setText('')
    self.ui.input_priceBill.setText('')
    self.ui.input_quantityBill.setText('')

    #Para empezar a crear una nueva factura
    self.ui.tableBill.setRowCount(0)
    newinvoicenumber(self)
    self.ui.label_valTotRES.setText("")

def buscarProductoEnInventarioPorId(self):
    
    cursor = CNXNSQL.conexion.cursor()
    setters.update_search_id(self.ui.input_searchStock.text())
    result = querys.getProductByID(cursor, variables.searchId)

    print (result)

def getListProduct(self):
    cursor = CNXNSQL.conexion.cursor()
    results = querys.getAllProducts(cursor)
    
    printStockTable.stockTable(self, results)

