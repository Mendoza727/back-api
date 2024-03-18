from db.db import *

# DTO user
class UserDto:
    def __init__(self, id, name, lastname, username, password, email, phone, age, IsDelete, IsActive, LastInsert, LastUpdate):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.age = age
        self.IsDelete = IsDelete
        self.IsActive = IsActive
        self.LastInsert = LastInsert,
        self.LastUpdate = LastUpdate

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'phone': self.phone,
            'age': self.age,
            'IsDelete': self.IsDelete,
            'IsActive': self.IsActive,
            'LastInsert': self.LastInsert,
            'LastUpdate': self.LastUpdate
        }


def authentication(email, password):
    #conexion con la base de datos
    conn = connect_to_database()

    try:
        with conn.cursor() as cursor:
            query = "SELECT id, name, lastname, username, password, email, phone, age, IsDelete, IsActive, LastInsert, LastUpdate FROM usuarios WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user_data = cursor.fetchone()
            if user_data is not None:
                user_dto = UserDto(*user_data)
                return user_dto.to_dict()
    finally:
        close_connection_to_database(conn)

    return None

if __name__ == '__main__':
    authentication()
