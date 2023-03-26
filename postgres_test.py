# Connect to your postgres DB
import psycopg2 as psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect("dbname=test user=postgres password=daniel")


    # Open a cursor to perform database operations
    cur = conn.cursor()

    create_table_query = '''CREATE TABLE mobile
              (ID INT PRIMARY KEY     NOT NULL,
              MODEL           TEXT    NOT NULL,
              PRICE         REAL); '''
    # Execute a command: this creates a new table
    cur.execute(create_table_query)
    conn.commit()
    print("Table created successfully in PostgreSQL ")
    # Execute a query
    cur.execute("SELECT * FROM my_data")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
    conn = psycopg2.connect("dbname=test user=postgres password=daniel")
    # Open a cursor to perform database operations
    cur = conn.cursor()
finally:
    cur.execute("SELECT * from mobile")
    print("Result ", cur.fetchall())

    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")