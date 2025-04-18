import time
import psycopg2
import os

host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")
user = os.getenv("DB_USER", "user")
password = os.getenv("DB_PASSWORD", "password")
database = os.getenv("DB_NAME", "etl_db")

while True:
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=database
        )
        conn.close()
        print("✅ Conexión a la base de datos exitosa.")
        break
    except psycopg2.OperationalError:
        print("⏳ Esperando a que la base de datos esté lista...")
        time.sleep(2)