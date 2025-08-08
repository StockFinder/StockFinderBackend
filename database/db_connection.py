import os
import psycopg2

HOSTNAME = os.environ.get("HOSTNAME", False)
DATABASE = os.environ.get("POSGRESQL_DATABASE")
USER     = os.environ.get("POSGRESQL_USER")
PASSWORD = os.environ.get("POSGRESQL_PASSWORD")
URL      = os.environ.get("POSGRESQL_URL")
PORT     = os.environ.get("POSGRESQL_PORT")

def sql_connection():
  connection = psycopg2.connect(user=USER, password=PASSWORD, host=URL, port=PORT, database=DATABASE)
  return connection
