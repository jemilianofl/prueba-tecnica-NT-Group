import pandas as pd
from sqlalchemy import create_engine, text
from db_engine import get_engine

engine = get_engine()

# Leer el CSV transformado
df = pd.read_csv("transformed_data.csv", parse_dates=["created_at", "updated_at"])

with engine.connect() as conn:
    conn.execute(text("""
        DROP TABLE IF EXISTS charges, companies;

        CREATE TABLE companies (
            id VARCHAR(24) PRIMARY KEY,
            name VARCHAR(130)
        );

        CREATE TABLE charges (
            id VARCHAR(24) PRIMARY KEY,
            company_id VARCHAR(24) REFERENCES companies(id),
            amount DECIMAL(16,2) NOT NULL,
            status VARCHAR(30) NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP
        );
    """))

# Insertar a través de pandas
df_companies = df[["company_id", "company_name"]].drop_duplicates().rename(
    columns={"company_id": "id", "company_name": "name"}
)
df_charges = df.drop(columns=["company_name"])

df_companies.to_sql("companies", engine, if_exists="append", index=False)
df_charges.to_sql("charges", engine, if_exists="append", index=False)

print("Base de datos estructurada y cargada.")
