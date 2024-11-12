import psycopg2

conn = psycopg2.connect(
    dbname="pythondb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Cursor para operar con la base de datos
cur = conn.cursor()

cur.execute("SELECT * FROM users")

records = cur.fetchall()

print(records)