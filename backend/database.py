import psycopg2
import os
import time

def get_connection():
    max_retries = 10
    retry_delay = 2  # seconds

    for i in range(max_retries):
        try:
            return psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB", "todo_db"),
                user=os.getenv("POSTGRES_USER", "postgres"),
                password=os.getenv("POSTGRES_PASSWORD", "postgres"),
                host=os.getenv("POSTGRES_HOST", "db"),
                port=os.getenv("POSTGRES_PORT", "5432")
            )
        except psycopg2.OperationalError as e:
            print(f"[Attempt {i+1}] Database not ready yet: {e}")
            time.sleep(retry_delay)

    raise Exception("Could not connect to the PostgreSQL database after several retries.")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

