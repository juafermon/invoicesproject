import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        port="5432",
        database="db_invoices",
        user="postgres",
        password="12345678"
    )
    print ("tamos conectados")

    cursor = conexion.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()

except Exception as error:
    print("error al conectar", error)

# finally:
#     if 'conexion' in locals() and conexion:
#         conexion.close()
#         print("conexion cerrada")