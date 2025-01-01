import psycopg2

# Conexão ao banco
conn = psycopg2.connect(
    dbname="ecommerce_db",
    user="your_username",
    password="your_password",
    host="localhost"
)

query = """
    SELECT category, SUM(amount * price) AS total_revenue
    FROM sales
    JOIN products ON sales.product_id = products.product_id
    GROUP BY category
    ORDER BY total_revenue DESC;
"""
cur = conn.cursor()
cur.execute(query)
results = cur.fetchall()

# Exibir resultados
for row in results:
    print(row)

cur.close()
conn.close()
