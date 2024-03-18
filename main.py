from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

#import views
from src.auth import auth
from src.gestionEventos import viewEventos
from src.seguimientoGastos import viewGastos
from src.gestionInventario import viewInventario
from src.reservaCitas import viewCitas

#dtos
from src.gestionEventos.viewEventos import EventDTO
from src.gestionInventario.viewInventario import ProductoDTO
from src.reservaCitas.viewCitas import CitaDTO
from src.seguimientoGastos.viewGastos import GastoDTO

app = Flask(__name__)
CORS(app, support_credentials=True)

# login
@app.route('/auth', methods=['POST', 'GET'])
def login():
    data = request.json
    #pasamos los datos al view
    login = auth.authentication(data['email'], data['password'])

    if login is not None:
        return jsonify({
            'status': 'success',
            'message': 'Usuario autenticado correctamente',
            'user': login
        }), 200
    else:
         return jsonify({
            'status': 'error',
            'message': 'Credenciales incorrectas'
        }), 401


#servicio 1
    # este serivicio gestiona todo lo relacionado a inventario
    # crear inventario y visualizarlos
    # ver productos y crearlos
@app.route('/gestion-inventario', methods=['POST', 'GET'])
def gestionInventario():
    data = request.json

    if 'save_producto' in data:

        # creamos el objeto para guardarlo en la base de datos
        event_dto = ProductoDTO(
            id=None,
            nombre=data['nombre'],
            cantidad=data['cantidad'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            proveedor=data['proveedor']
        )

        producto_id = viewInventario.create_producto(event_dto)

        if producto_id:
            return jsonify({
                'status': 'success',
                'message': 'Producto creado con éxito',
                'id': producto_id
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Hubo un error al crear el producto'
            }), 401
    
    if 'consult_productos' in data:
        productos = viewInventario.get_all_productos()

        if productos:
            return jsonify({
                'status': 'success',
                'message': 'Productos consultados con éxito',
                'productos': productos
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Hubo un error al consultar los productos'
            }), 401


# servicio 2
    # gestion de eventos
    # crear y consultar eventos
@app.route('/gestion-eventos', methods=['POST', 'GET'])
def gestionEventos():
    data = request.json
    print(data)
    
    if 'save' in data:
        if data['save']:
            if 'event' in data and data['event']:
                # Creamos el dato
                event_dto = EventDTO(
                    id=None,
                    titulo=data['titulo'],
                    descripcion=data['descripcion'],
                    fecha=data['fecha'],
                    hora=data['hora'],
                    ubicacion=data['ubicacion']
                )

                # Guardamos el evento
                saveEvent = viewEventos.create_events(event_dto)
                if saveEvent is not None:
                    return jsonify({
                        'status': 'success',
                        'message': 'Evento creado con éxito',
                        'id': saveEvent 
                    }), 200
                else:
                    return jsonify({
                        'status': 'error',
                        'message': 'Hubo un error al crear el evento',
                    }), 401
            else:
                # Consultamos todos los eventos
                consultEvent = viewEventos.get_all_event()
                if consultEvent is not None:
                    return jsonify({
                        'status': 'success',
                        'message': 'Eventos consultados con éxito',
                        'events': consultEvent 
                    }), 200
                else:
                    return jsonify({
                        'status': 'error',
                        'message': 'Hubo un error al consultar los eventos',
                    }), 401
        else:
            if 'consultEvent' in data and data['consultEvent']:
                # Consultamos todos los eventos
                consultEvent = viewEventos.get_all_event()
                if consultEvent is not None:
                    return jsonify({
                        'status': 'success',
                        'message': 'Eventos consultados con éxito',
                            'events': consultEvent 
                    }), 200
                else:
                    return jsonify({
                        'status': 'error',
                        'message': 'Hubo un error al consultar los eventos',
                    }), 401
            else:
                # Consultamos todos los asistentes
                consultAssist = viewEventos.get_all_assist()
                if consultAssist is not None:
                    return jsonify({
                        'status': 'success',
                        'message': 'Asistentes consultados con éxito',
                        'assistants': consultAssist 
                    }), 200
                else:
                    return jsonify({
                        'status': 'error',
                        'message': 'Hubo un error al consultar los asistentes',
                    }), 401
    else:
        return jsonify({
            'status': 'error',
            'message': 'Operación no válida',
        }), 400



# podras crar citas y consultarlas 
@app.route('/reserva-citas', methods=['POST', 'GET'])
def reservaCitas():
    if request.method == 'POST':
        data = request.json

        if 'crear_cita' in data:
            fecha = data['fecha'] = datetime.now().strftime("%Y-%m-%d")
            
            # construimos el objeto
            cita_dto = CitaDTO(
                id_usuario=data['id_usuario'],
                tipo_cita=data['tipo_cita'],
                hora=data['hora'],
                fecha=fecha,
                nota=data['nota']
            )

            cita_id = viewCitas.crear_cita(cita_dto)

            if cita_id:
                return jsonify({
                    'status': 'success',
                    'message': 'Cita creada con éxito',
                    'id': cita_id
                }), 200
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Hubo un error al crear la cita'
                }), 401

        elif 'consultar_cita' in data:
            cita_consultada = viewCitas.obtener_todas_las_citas()

            if cita_consultada:
                return jsonify({
                    'status': 'success',
                    'message': 'Cita consultada con éxito',
                    'cita': cita_consultada
                }), 200
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Hubo un error al consultar la cita'
                }), 404
        
@app.route('/seguimiento-gastos', methods=['POST', 'GET'])
def seguimientoGastos():
    if request.method == 'POST':
        data = request.json

        if 'crear_gasto' in data:
            fecha = data['fecha'] = datetime.now().strftime("%Y-%m-%d")

            #creamos el objeto
            gasto_dto = GastoDTO(
                categoria=data['categoria'],
                concepto=data['concepto'],
                descripcion=data['descripcion'],
                fecha=fecha,
                monto=data['monto']
            )

            gasto_id = viewGastos.create_gasto(gasto_dto)

            if gasto_id:
                return jsonify({
                    'status': 'success',
                    'message': 'Gasto creado con éxito',
                    'id': gasto_id
                }), 200
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Hubo un error al crear el gasto'
                }), 401
            
        elif 'consultar_gasto':
            gastos = viewGastos.get_all_gastos()

        if gastos:
            return jsonify({
                'status': 'success',
                'message': 'Gastos obtenidos con éxito',
                'gastos': gastos
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Hubo un error al obtener los gastos'
            }), 401
        
# ejecutamos el servidor desde el servicio principal
if __name__ == '__main__':
    app.run(debug=True)
    