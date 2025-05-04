
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from Funciones import restricciones, setters, calculos
from Variables import variables
from PyQt5 import QtWidgets

    #Obtener valores en Qlineedit seccion Bills y tabla
def getValuesBills (self):

    setters.update_cc(self.ui.input_CCBill.text())
    setters.update_nameClient(self.ui.input_nameCLientBill.text())
    setters.update_email(self.ui.input_emailBill.text())
    setters.update_idProd(self.ui.input_idProdBill.text())
    setters.update_quantity(self.ui.input_quantityBill.text().strip())
    setters.update_price(self.ui.input_priceBill.text())
    setters.update_inv_number(self.ui.label_actualinvnum.text())

    print(variables.invoice_num, "printttt en get values")

    #setters.update_nameProd = self.ui.input_nameProdBill.text()
    if(variables.quantity != ''):
            Subtotal = str(int(variables.quantity)*int(variables.price))

            arrayValues = []
            #arrayValues.append(self.ui.input_CCBill.text())
            #arrayValues.append(self.ui.input_nameCLientBill.text())
            #arrayValues.append(self.ui.input_emailBill.text())
            arrayValues.append(variables.idProd)
            arrayValues.append('nombree')
            #arrayValues.append(querys.productname(cursor, IdProd))
            arrayValues.append(variables.price)
            arrayValues.append(variables.quantity)
            arrayValues.append(Subtotal)
            
            actualrows = self.ui.tableBill.rowCount()
            self.ui.tableBill.insertRow(actualrows)

            for i, value in enumerate (arrayValues):
                item = QtWidgets.QTableWidgetItem(value)
                self.ui.tableBill.setItem(actualrows, i, item)

            calculos.operTable(self)

            # else:
            #     print("Error de entrada" )

            #agregar a tabla
            #querys.insertquery(cursor, "B001", "2", "200", "1000", "2025-04-30")
            #CNXNSQL.conexion.commit()

    
        

    restricciones.campoProducto(self, variables.idProd)
    restricciones.campoQuantity(self, variables.quantity)

#Funcion para eliminar de tabla
def deleteValuesTable (self):
    actualrows = self.ui.tableBill.rowCount()
    self.ui.tableBill.removeRow(actualrows-1)
    calculos.operTable(self)
    
    
    #reset de los campos
    # self.ui.input_idProdBill.setText('')
    # self.ui.input_priceBill.setText('')
    # self.ui.input_quantityBill.setText('')


def generarFactura_pdf(self):
        #cursor = CNXNSQL.conexion.cursor()

        # 1. Recopilacion de datos
        invoice_info = {
            "numero_factura": variables.invoice_num,
            #"fecha_factura": self.ui.inputDateBill.text(),
            "nombre_cliente": variables.nameClient,
            "direccion_cliente": variables.email,
        }
        
        invoice_items = []

        num_rows = self.ui.tableBill.rowCount()
        for row in range(num_rows):
            producto = self.ui.tableBill.item(row, 0).text() if self.ui.tableBill.item(row, 0) else ""
            cantidad = self.ui.tableBill.item(row, 1).text() if self.ui.tableBill.item(row, 1) else ""
            precio_unitario = self.ui.tableBill.item(row, 2).text() if self.ui.tableBill.item(row, 2) else ""
            precio_total = self.ui.tableBill.item(row, 3).text() if self.ui.tableBill.item(row, 3) else ""
            #numero_factura = variables.invoice_num
            invoice_items.append({
                "producto": producto,
                "cantidad": cantidad,
                "precio_unitario": precio_unitario,
                "precio_total": precio_total,
            })

            
            total_factura = sum(float(item["precio_total"]) for item in invoice_items if item["precio_total"])


        print(invoice_info, "factura info")
                # 2. Renderizar la plantilla HTML con los datos
        env = Environment(loader=FileSystemLoader('.')) # Asume que la plantilla está en el mismo directorio
        template = env.get_template('GUI/invoice/invoice.html')
        html = template.render(
            factura_info=invoice_info,
            items=invoice_items,
            total_factura=total_factura
            )

        # 3. Convertir el HTML a PDF usando xhtml2pdf
        filename = "facturagenerada.pdf"
        with open(filename, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(html, dest=pdf_file)
            if pisa_status.err:
                print(f"Error al generar el PDF: {pisa_status.err}")
            else:
                print(f"Factura generada {filename}")