from db.db import *

# conexion a la base de datos
conn = connect_to_database()

# DTO Productos
class ProductoDTO: 
    def __init__(self, id, nombre, descripcion, precio, cantidad, proveedor):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion 
        self.precio = precio
        self.cantidad = cantidad
        self.proveedor = proveedor

# DTO Registro de Inventario
class RegistroInventarioDTO:
    def __init__(self,id_producto, tipo_operacion, cantidad, fecha_registro,id=None):
        self.id = id
        self.id_producto = id_producto
        self.tipo_operacion = tipo_operacion
        self.cantidad = cantidad
        self.fecha_registro = fecha_registro

def to_dict(self):
    return vars(self)
        

def create_producto(producto_dto: ProductoDTO):
    try:
        with conn.cursor() as cursor:
            # insertamos en la base de datos
            sql = "INSERT INTO Productos (nombre, descripcion, precio, cantidad, proveedor) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (producto_dto.nombre, producto_dto.descripcion, producto_dto.precio, producto_dto.cantidad, producto_dto.proveedor))
            conn.commit()
            return cursor.lastrowid
    finally:
        close_connection_to_database(conn)

def get_all_productos():
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Productos"
            cursor.execute(sql)
            productos_data = cursor.fetchall()
            productos = []
            for producto_data in productos_data:
                # creamos el objeto
                producto = ProductoDTO(*producto_data)
                productos.append(producto)
            return [to_dict(producto) for producto in productos]
    finally:
        close_connection_to_database(conn)

if __name__ == '__main__':
    create_producto()
    get_all_productos()