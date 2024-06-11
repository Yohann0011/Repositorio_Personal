#pip install necesarios
#pip install mysql-connector-python

"""
========================================================================
---------------------------| IMPORTACIONES |----------------------------
========================================================================
"""
import mysql.connector

"""
========================================================================
-----------------------------| VARIABLES |------------------------------
========================================================================
"""
nombreTabla = "usuarios"
"""
========================================================================
-----------------------------| FUNCIONES |------------------------------
========================================================================
"""
# Conexión a la base de datos MySQL
def connect_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )

# Crear
def create_mysql(cursor, nombreTabla):
    query = "INSERT INTO {} (nombre, correo) VALUES (%s, %s)".format(nombreTabla)
    cursor.execute(query, ("Juan Perez", "juan.perez@example.com"))

# Leer
def read_mysql(cursor, table_name):
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    for (id, nombre, correo) in cursor:
        print(f"{id}, {nombre}, {correo}")

# Actualizar
def update_mysql(cursor, table_name):
    query = "UPDATE {} SET correo = %s WHERE nombre = %s".format(table_name)
    cursor.execute(query, ("juan.nuevo@example.com", "Juan Perez"))

# Eliminar
def delete_mysql(cursor, table_name):
    query = "DELETE FROM {} WHERE nombre = %s".format(table_name)
    cursor.execute(query, ("Juan Perez",))

"""
========================================================================
-----------------------------| LÓGICA |---------------------------------
========================================================================
"""
# Ejecución del CRUD
conexion = connect_mysql()
puntero = conexion.cursor()

create_mysql(puntero, nombreTabla)
read_mysql(puntero, nombreTabla)
update_mysql(puntero, nombreTabla)
delete_mysql(puntero, nombreTabla)

conexion.commit()
puntero.close()
conexion.close()





