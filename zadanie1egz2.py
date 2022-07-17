from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

DB = "create database exam2;"
user = "postgres"
password = "Poczta3241567"
host = "localhost"

try:
    connect = connect(user=user, password=password,host=host)
    connect.autocommit = True
    cursor = connect.cursor()
    try:
        cursor.execute(DB)
        print('Baza utworzona')
    except DuplicateDatabase as base_in:
        print('Data Base exists', base_in)
except OperationalError as errr:
    print('Wyjebało błąd i jest swąd:', errr)
