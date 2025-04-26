import psycopg2
import dotenv

try:

    DATABASE_URL= "postgresql://neondb_owner:npg_W0xXfdKstSM5@ep-raspy-pine-a4gtnxno-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

    conexion = psycopg2.connect(
        DATABASE_URL
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