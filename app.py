import psycopg2
import csv

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "Vicky120600*",
    database = "test",
    port = "5432"
)

connection.autocommit = True

def crear_tabla():
    cursor = connection.cursor()
    query = "CREATE TABLE personas(id int8,first_name varchar(255),last_name varchar(255), email varchar (255), gender varchar(255), ip_address varchar(255))"
    try:
        cursor.execute(query)
    except:
        print("La tabla ya existe")
    cursor.close()


def leer_archivo():
    persona = []
    with open("todas_personas.csv") as archivo:
        datos = csv.reader(archivo, delimiter=",")
        for linea in datos:
            persona.append(linea)
    del(persona[0])
    return persona
    

def insertar_datos(datos):
    cursor = connection.cursor()
    for i in datos:
        first_name = i[1].replace("'",'"')
        last_name = i[2].replace("'",'"')
        query = f"""INSERT INTO personas(id,first_name,last_name, email, gender, ip_address) values ({i[0]}, '{first_name}', '{last_name}', '{i[3]}', '{i[4]}', '{i[5]}')"""
        cursor.execute(query)
    cursor.close()

if __name__ == "__main__":
    crear_tabla()
    datos = leer_archivo()
    insertar_datos(datos)