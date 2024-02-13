import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(os.getenv("CONN_STRING"))
    print("Connected to the database successfully")
except Exception as e:
    print("Unable to connect to the database:", e)

if __name__ == "__main__":
    print("Hello World")
