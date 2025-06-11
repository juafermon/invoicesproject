from jinja2 import Environment, FileSystemLoader
#from xhtml2pdf import pisa
from weasyprint import HTML, CSS 
from src.database import querys
from src.database.CNXNSQL import conexion
from src.core import variables, utils
from PyQt5.QtWidgets import QMessageBox
import os

cursor = conexion.cursor()

# Function to calculate total bill 
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

def createBill(self):
    #cursor = CNXNSQL.conexion.cursor()
    invoice_info = {
        "numero_factura": variables.invoice_num,
        "fecha_factura": variables.invoice_date.strftime("%Y %m %d"),
        "nombre_cliente": variables.nameClient,
        "correo_cliente": variables.email,
        "identificacion_cliente": variables.cc,
    }
    
    invoice_items = []

    num_rows = self.ui.tableBill.rowCount()
    for row in range(num_rows):
        idProduct = self.ui.tableBill.item(row, 0).text() if self.ui.tableBill.item(row, 0) else ""
        product = self.ui.tableBill.item(row, 1).text() if self.ui.tableBill.item(row, 1) else ""
        quantity = self.ui.tableBill.item(row, 2).text() if self.ui.tableBill.item(row, 2) else ""
        unitPrice = self.ui.tableBill.item(row, 3).text() if self.ui.tableBill.item(row, 3) else ""
        totalPrice = self.ui.tableBill.item(row, 4).text() if self.ui.tableBill.item(row, 4) else ""
        invoice_items.append({
            "id_producto": idProduct,
            "producto": product,
            "cantidad": quantity,
            "precio_unitario": unitPrice,
            "precio_total": totalPrice,
        })
   
        totalBill = sum(float(item["precio_total"]) for item in invoice_items if item["precio_total"])
        
        result = querys.getProductByID(cursor, idProduct)
        diff = result[0][3]-int(quantity)
        querys.updateStockProducts(cursor, diff, idProduct) #Update stock in products table
        querys.insertInfoInvoiceTable(cursor,idProduct, quantity,totalPrice,totalBill,variables.invoice_date,variables.invoice_num)   

        conexion.commit()


#   Render template HTML with data
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, '..', 'GUI', 'invoice')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('invoice.html')
    html = template.render(
        factura_info=invoice_info,
        items=invoice_items,
        total_factura=totalBill
        )

    # Conversion with Weasyprint
    filename = f"{variables.invoice_num}{variables.invoice_date.strftime("%Y %m %d").replace(" ","")}.pdf"
    full_pdf_path = os.path.join("PDFs", filename)
    os.makedirs("PDFs", exist_ok=True) # FOLDER PDFs

    html_doc = HTML(string=html, base_url=template_dir)

    # upload of CSS
    css_path = os.path.join(template_dir, 'style.css')
    css_doc = CSS(filename=css_path) 

    try:
        html_doc.write_pdf(full_pdf_path, stylesheets=[css_doc])
        print(f"Factura generada {filename}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")


    utils.cleanBillTable(self)
    utils.newBill(self)
    results = querys.getAllProducts(cursor)
    utils.stockTable(self, results)
