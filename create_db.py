import os
import psycopg2
import threading
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from database.db_connection import USER, PASSWORD, DATABASE, URL, PORT
from database.stockfinder_models import base as db_base


def crear_base_de_datos():
    conn = psycopg2.connect(dbname="postgres", user=USER, password=PASSWORD, host=URL, port=PORT)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (DATABASE,))
    exists = cursor.fetchone()

    if not exists:
        print(f"🛠️  Creando base de datos '{DATABASE}'...")
        cursor.execute(f"CREATE DATABASE {DATABASE};")
        crear_tablas()
    else:
        print(f"✅ La base de datos '{DATABASE}' ya existe.")

    cursor.close()
    conn.close()

def crear_tablas():
    print("📑 Creando tablas...")
    engine = db_base.get_engine()
    db_base.get_session()
    db_base.Base.metadata.create_all(engine)
    print("✅ Tablas creadas correctamente.")


def when_ready(server):
    print("🔧 Gunicorn está listo. Creando tablas en PostgreSQL si no existen...")
    hilo = threading.Thread(target=crear_base_de_datos)
    hilo.start()