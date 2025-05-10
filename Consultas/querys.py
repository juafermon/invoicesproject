from Comunicaciones import CNXNSQL

#Consulta para insertar la informacion en la tabla invoices
def insertInfoInvoiceTable(cursor, product_id, qty, price, total_amount, invoice_date, invoice_number):
    cursor.execute(
        "INSERT INTO invoices (product_id, qty, price, total_amount, invoice_date, invoice_number) VALUES (%s, %s, %s, %s, %s, %s)", (product_id, qty, price, total_amount, invoice_date, invoice_number)
        )

#Consulta para obtener el nombre del producto desde la tabla products
def getProductName(cursor, product_id):
    cursor.execute(
        """SELECT product_name FROM public.products WHERE product_id=%s;""",(product_id,)
    )
    result = cursor.fetchone()
    return result[0] if result is not None else ''

def invoicenumber(cursor):
    cursor.execute(
        """SELECT MAX (invoice_number) FROM public.invoices"""
    )
    result = cursor.fetchone()
    return result[0]