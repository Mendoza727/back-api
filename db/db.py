import pymysql

def connect_to_database():
    # datos de la conexion
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'password',
        'database': 'db_prueba2',
        'port': 3306
    }

    try:
        #establecemos conexion
        conn = pymysql.connect(**db_config)
        print('Conexion a la base de datos exitosa')
        return conn
    except pymysql.Error as e:
        print('Error al conectar con la base de datos', e)
        return e
    
def close_connection_to_database(conn):
    if conn:
        # cerramos la conexion si existe
        conn.close()
        print('Conexion Cerrada')


if __name__ == '__main__':
    connect_to_database()
    close_connection_to_database()