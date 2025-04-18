import pandas as pd
from sqlalchemy import create_engine
from db_engine import get_engine

try:
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM raw_data", engine)
    df.to_csv("extracted_data.csv", index=False)
    print("✅ Extracción completada, archivo guardado como 'extracted_data.csv'.")
except Exception as e:
    print(f"❌ Error en extract_data.py: {e}")