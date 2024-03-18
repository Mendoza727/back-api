from db.db import *

# conexion a la base de datos
#conn = connect_to_database()

# DTO Gastos
class GastoDTO: 
    def __init__(self, concepto, categoria, monto, fecha, descripcion, id=None):
        self.id = id
        self.concepto = concepto
        self.categoria = categoria 
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion

def to_dict(self):
    return vars(self)
        

def create_gasto(gasto_dto: GastoDTO):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            # insertamos en la base de datos
            sql = "INSERT INTO Gastos (concepto, categoria, monto, fecha, descripcion) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (gasto_dto.concepto, gasto_dto.categoria, gasto_dto.monto, gasto_dto.fecha, gasto_dto.descripcion))
            conn.commit()
            return cursor.lastrowid
    finally:
        close_connection_to_database(conn)

def get_all_gastos():
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT concepto, categoria, monto, fecha, descripcion, id FROM Gastos"
            cursor.execute(sql)
            gastos_data = cursor.fetchall()
            gastos = []
            for gasto_data in gastos_data:
                # creamos el objeto
                gasto = GastoDTO(*gasto_data)
                gastos.append(gasto)
            return [to_dict(gasto) for gasto in gastos]
    finally:
        close_connection_to_database(conn)

if __name__ == '__main__':
    create_gasto()
    get_all_gastos()
