import os
from sqlalchemy import create_engine

def get_engine():
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    user = os.getenv("DB_USER", "user")
    password = os.getenv("DB_PASSWORD", "password")
    database = os.getenv("DB_NAME", "etl_db")

    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")