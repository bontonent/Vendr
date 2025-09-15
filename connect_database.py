import psycopg2
import os


def connect_to_db():
    conn = psycopg2.connect(
        dbname = "vendr",
        user = "postgres",
        password = os.getenv('db_password'),
        port = os.getenv('db_port'),
        host = os.getenv('db_host')
    )
    cur = conn.cursor()
    return conn, cur
# create new row
def create_row(name_company,min_salary, mad_salary, max_salary, describe):
    conn, cur = connect_to_db()
    cur.execute(
        f"INSERT INTO products(name_company,min_salary, mad_salary, max_salary, describe) "
        f"VALUES(%s,%s,%s,%s,%s)",(name_company,min_salary,mad_salary,max_salary,describe))
    conn.commit()

    cur.close()


# delete all rows
def delete_all_rows():
    conn, cur = connect_to_db()
    cur.execute("DELETE FROM products")
    conn.commit()
    print("complete delete")

    cur.close()

# view all rows
def view_all_rows():
    conn, cur = connect_to_db()
    # view element
    cur.execute("SELECT * FROM products")
    db_version = cur.fetchone()
    print(db_version)

    cur.close()



