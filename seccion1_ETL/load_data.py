import pandas as pd
from sqlalchemy import create_engine
from db_engine import get_engine

try:
    # Lee el archivo CSV
    df = pd.read_csv("data/data_prueba_tecnica.csv")

    # Crea engine PostgreSQL (ajusta si cambias credenciales o nombre de servicio)
    engine = get_engine()

    # Guarda en base de datos
    df.to_sql("raw_data", engine, if_exists="replace", index=False)

    print("✅ Datos cargados correctamente a la tabla 'raw_data'.")

except Exception as e:
    print(f"❌ Error en load_data.py: {e}")