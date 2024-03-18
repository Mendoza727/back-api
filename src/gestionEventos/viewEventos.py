from db.db import *

# conexion a la base de datos


# DTO events
class EventDTO: 
    def __init__(self,titulo,descripcion ,fecha ,hora ,ubicacion, id=None):
        self.titulo = titulo
        self.descripcion = descripcion 
        self.fecha = fecha
        self.hora = hora
        self.ubicacion = ubicacion

from .viewEventos import EventDTO

class Asistant:
    def __init__(self, id,id_evento,id_usuario,nombre,edad,contact,email):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.edad = edad
        self.contact = contact
        self.email = email


def to_dict(self):
    return vars(self)
        
def create_events(event_dto: EventDTO):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # insertamos en la base de datos
            sql = "INSERT INTO eventos (titulo, descripcion, fecha, hora, ubicacion) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (event_dto.titulo, event_dto.descripcion, event_dto.fecha, event_dto.hora, event_dto.ubicacion))
            conn.commit()
            return cursor.lastrowid
    finally:
        close_connection_to_database(conn)

def get_all_event():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT titulo, descripcion, fecha, hora, ubicacion FROM eventos"
            cursor.execute(sql)
            events_data = cursor.fetchall()
            events = []
            for event_data in events_data:
                # creamos el objeto
                event = EventDTO(*event_data)
                events.append(event)
            return [to_dict(event) for event in events]         
    finally:
        close_connection_to_database(conn)


def create_assits(asssitant: Asistant):
    conn = connect_to_database()
    try: 
        with conn.cursor() as cursor:
            #insertamos en la base de datos
            sql = "INSERT INTO asistentes (id_evento, id_usuario, nombre, edad, contacto, email) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (asssitant.id_evento, asssitant.id_usuario, asssitant.nombre, asssitant.edad, asssitant.contact, asssitant.email))
            conn.commit()
            return cursor.lastrowid
    finally:
        close_connection_to_database()


def get_all_assist():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM asistentes"
            cursor.execute(sql)
            assistants_data = cursor.fetchall()
            assistants = []
            for assistant_data in assistants_data:
                # creamos el objeto
                assistant = Asistant(*assistant_data)
                assistants.append(assistant)
                return [to_dict(assistant) for assistant in assistant]
    finally:
        close_connection_to_database()

def analisi_event():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            return None
    finally:
        close_connection_to_database()

if __name__ == '__main__':
    create_events()
    create_assits()
    get_all_assist()
    get_all_event()