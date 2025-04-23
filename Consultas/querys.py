from Comunicaciones import CNXNSQL

def insertquery(cursor, product_name, product_id):
    cursor.execute(
        "INSERT INTO invoices (product_name, product_id) VALUES (%s, %s)", (product_name, product_id)
        )
    