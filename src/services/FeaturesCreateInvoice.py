from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from src.database import querys
from src.database.CNXNSQL import conexion
from src.core import variables, utils
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
        "direccion_cliente": variables.email,
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
        
        querys.insertInfoInvoiceTable(cursor,idProduct, quantity,totalPrice,totalBill,variables.invoice_date,variables.invoice_num)
        
        conexion.commit()


# 2. Render template HTML with data
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, '..', 'GUI', 'invoice')
    env = Environment(loader=FileSystemLoader(template_dir)) # Asume que la plantilla está en el mismo directorio
    template = env.get_template('invoice.html')
    html = template.render(
        factura_info=invoice_info,
        items=invoice_items,
        total_factura=totalBill
        )
    

    # 3. Convertir el HTML a PDF usando xhtml2pdf
    filename = f"{variables.invoice_num}{variables.invoice_date.strftime("%Y %m %d").replace(" ","")}.pdf"
    full_pdf_path = os.path.join("PDFs", filename)
    with open(full_pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html, dest=pdf_file)
        if pisa_status.err:
            print(f"Error al generar el PDF: {pisa_status.err}")
        else:
            print(f"Factura generada {filename}")


    utils.cleanBillTable(self)
    utils.newBill(self)
    results = querys.getAllProducts(cursor)
    utils.stockTable(self, results)



def updateStockAfterCreateBill(self):    
    rows = self.ui.tableBill.rowCount()
    idProdArray = []
    selledQuantityArray = []
    for i in range(rows):
        itemIdProd = self.ui.tableBill.item(i, 0)
        itemQuantityArray = self.ui.tableBill.item(i, 3)

        idProdArray.append(itemIdProd.text())
        selledQuantityArray.append(itemQuantityArray.text())

    #for to get actual stock on products
    actualStockArray = []
    for i in range (len(idProdArray)):
        result = querys.getProductByID(cursor, idProdArray[i])
        actualStockArray.append(result[0][3])
    
    #FOR to get substract the stock on products
    substratedQuantityArray = []
    for i in range (len(idProdArray)):
        Substract = int(actualStockArray[i])-int(selledQuantityArray[i])
        substratedQuantityArray.append(Substract)

    #FOR to update stock by product id in products Table
    for i in range(len(substratedQuantityArray)):
        querys.updateStockProducts(cursor, substratedQuantityArray[i], idProdArray[i])