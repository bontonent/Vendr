# If you would like see what the DB I use
# ./SQL_script/vendr.sql

import psycopg2
import os


def connect_to_db():
    # Connect DB
    conn = psycopg2.connect(
        dbname = "vendr",
        user = "postgres",
        password = os.getenv('db_password'),
        port = os.getenv('db_port'),
        host = os.getenv('db_host')
    )
    cur = conn.cursor()

    # Return instrument DB
    return conn, cur

# Create new row in DB
def create_row(name_company,min_salary, mad_salary, max_salary, describe):
    # Connect to DB
    conn, cur = connect_to_db()

    # Script
    cur.execute(
        f"INSERT INTO products(name_company,min_salary, mad_salary, max_salary, describe) "
        f"VALUES(%s,%s,%s,%s,%s)",(name_company,min_salary,mad_salary,max_salary,describe))
    conn.commit()

    # Close DB
    cur.close()

# Don't using
# ----
# Delete all rows
def delete_all_rows():
    # Connect to DB
    conn, cur = connect_to_db()

    # Script
    cur.execute("DELETE FROM products")
    conn.commit()

    # Close DB
    cur.close()
    print("complete delete")

# View all rows
def view_all_rows():
    # Connect to DB
    conn, cur = connect_to_db()

    # Script
    cur.execute("SELECT * FROM products")

    #View
    db_version = cur.fetchone()
    print(db_version)

    # Close DB
    cur.close()



