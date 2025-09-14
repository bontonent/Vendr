import psycopg2
import os



con = psycopg2.connect(
    dbname = "vendr",
    user = "postgres",
    password = os.getenv('db_password'),
    port = os.getenv('db_port'),
    host = os.getenv('db_host')


)

cur = con.cursor()

cur.execute("SELECT * FROM products")
db_version = cur.fetchone()
print(db_version)
cur.close()