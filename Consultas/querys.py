from Comunicaciones import CNXNSQL
from GUI.gui import Ui_MainWindow

def insertquery(cursor, product_id, qty, price, total_amount, invoice_date):
    cursor.execute(
        "INSERT INTO invoices (product_id, qty, price, total_amount, invoice_date) VALUES (%s, %s, %s, %s, %s)", (product_id, qty, price, total_amount, invoice_date)
        )
    
def productname(cursor, product_id):
    cursor.execute(
        """SELECT product_name FROM public.products WHERE product_id=%s;""",(product_id,)
    )
    result = cursor.fetchone()
    return result[0]
