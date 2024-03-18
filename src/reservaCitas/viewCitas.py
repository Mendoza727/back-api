from db.db import *

# conexión a la base de datos
conn = connect_to_database()

# DTO Citas
class CitaDTO: 
    def __init__(self, id, id_usuario, fecha, hora, nota):
        self.id = id
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.hora = hora
        self.nota = nota

def to_dict(self):
    return vars(self)
        

def crear_cita(cita_dto: CitaDTO):
    try:
        with conn.cursor() as cursor:
            # insertar en la base de datos
            sql = "INSERT INTO Citas (id_usuario, fecha, hora, nota) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (cita_dto.id_usuario, cita_dto.fecha, cita_dto.hora, cita_dto.nota))
            conn.commit()
            return cursor.lastrowid
    finally:
        close_connection_to_database(conn)

def obtener_todas_las_citas():
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Citas"
            cursor.execute(sql)
            citas_data = cursor.fetchall()
            citas = []
            for cita_data in citas_data:
                # crear el objeto
                cita = CitaDTO(*cita_data)
                citas.append(cita)
            return [to_dict(cita) for cita in citas]
    finally:
        close_connection_to_database(conn)

def analizar_citas():
    try:
        with conn.cursor() as cursor:
            return None
    finally:
        close_connection_to_database(conn)

if __name__ == '__main__':
    crear_cita()
    obtener_todas_las_citas()
