#Query to insert rows to invoice table
def insertInfoInvoiceTable(cursor, product_id, qty, price, total_amount, invoice_date, invoice_number):
    cursor.execute(
        "INSERT INTO invoices (product_id, qty, price, total_amount, invoice_date, invoice_number) VALUES (%s, %s, %s, %s, %s, %s)", (product_id, qty, price, total_amount, invoice_date, invoice_number)
        )

def invoicenumber(cursor):
    cursor.execute(
        """SELECT MAX (invoice_number) FROM public.invoices"""
    )
    result = cursor.fetchone()
    return result[0]

def getAllProducts(cursor):
    cursor.execute(
        """SELECT   product_id, product_name, price, stock FROM public.products"""
    )
    result = cursor.fetchall()
    return result

#Query to get product info
def getProductByID(cursor, product_id):
    cursor.execute(
        """SELECT product_id, product_name, price, stock FROM public.products WHERE product_id=%s;""",(product_id,)
    )
    result = cursor.fetchall()
    return result if result is not None else ''

def insertInfoProductTable(cursor, product_id, product_name, price, stock):
    cursor.execute(
        "INSERT INTO products (product_id, product_name, price, stock) VALUES (%s, %s, %s, %s)", (product_id, product_name, price, stock)
    )

def updateInfoProductTable(cursor,stock, price, product_id, product_name):
    cursor.execute(
        "UPDATE products SET stock = %s, price = %s, product_name = %s WHERE product_id = %s", (stock, price, product_name, product_id)
    )