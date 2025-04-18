from sqlalchemy import create_engine, text
from db_engine import get_engine

sql_script = """
CREATE OR REPLACE VIEW daily_company_transactions AS
SELECT 
    DATE(created_at) AS transaction_date,
    c.id AS company_id,
    c.name AS company_name,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM 
    charges ch
    JOIN companies c ON ch.company_id = c.id
GROUP BY 
    DATE(created_at), c.id, c.name
ORDER BY 
    transaction_date, c.id;
"""

engine = get_engine()
with engine.connect() as conn:
    conn.execute(text(sql_script))
    print("Vista daily_company_transactions creada exitosamente.")