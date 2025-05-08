from Comunicaciones import CNXNSQL

def insertInfoInvoiceTable(cursor, product_id, qty, price, total_amount, invoice_date, invoice_number):
    cursor.execute(
        "INSERT INTO invoices (product_id, qty, price, total_amount, invoice_date, invoice_number) VALUES (%s, %s, %s, %s, %s, %s)", (product_id, qty, price, total_amount, invoice_date, invoice_number)
        )
    
def productname(cursor, product_id):
    cursor.execute(
        """SELECT product_name FROM public.products WHERE product_id=%s;""",(product_id,)
    )
    result = cursor.fetchone()
    return result[0]

def invoicenumber(cursor):
    cursor.execute(
        """SELECT id_invoice FROM public.invoices ORDER BY id_invoice DESC"""
    )
    result = cursor.fetchone()
    return result[0]