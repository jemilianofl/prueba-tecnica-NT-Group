import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("extracted_data.csv")

# Renombrar columna 'name' a 'company_name'
df = df.rename(columns={"name": "company_name"})

# Convertir columnas de fecha
df["created_at"] = pd.to_datetime(df["created_at"], errors='coerce')

# Crear columna 'updated_at' como None (si no existe)
if "updated_at" not in df.columns:
    df["updated_at"] = pd.NaT  # NaT para tipo datetime

# Asegurar que 'amount' sea decimal
df["amount"] = pd.to_numeric(df["amount"], errors='coerce')

# Reordenar columnas y asegurarse de que estén todas
column_order = ["id", "company_name", "company_id", "amount", "status", "created_at", "updated_at"]
df = df[column_order]

# Guardar archivo transformado
df.to_csv("transformed_data.csv", index=False)

print("✅ Datos transformados exitosamente.")