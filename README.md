Backend Python para Gestión de Servicios
Este es un repositorio de backend Python para gestionar diferentes servicios, incluyendo:

Gestión de Eventos: Este servicio se encarga de administrar eventos, como fiestas, conferencias, reuniones, etc.

Gestión de Inventario: Este servicio se encarga de gestionar el inventario de productos o recursos disponibles en la organización.

Reserva de Citas: Este servicio permite a los usuarios reservar citas para diferentes propósitos, como consultas médicas, reuniones profesionales, etc.

Seguimiento de Gastos: Este servicio se encarga de realizar un seguimiento y registro de los gastos incurridos en la organización.

Tecnologías Utilizadas
Python
Flask (Framework web)

Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

app.py: Archivo principal que inicia la aplicación Flask y define las rutas principales.

Configuración
Clona este repositorio en tu máquina local.

git clone <url_del_repositorio>
Instala las dependencias necesarias utilizando pip.

pip install -r requirements.txt
Configura la conexión a la base de datos en el archivo de configuración config.py.

Ejecuta la aplicación Flask.
python app.py

Una vez que la aplicación esté en funcionamiento, puedes acceder a los diferentes servicios utilizando las rutas correspondientes. Por ejemplo:

Gestión de Eventos: src/eventos
Gestión de Inventario: src/inventario
Reserva de Citas: src/citas
Seguimiento de Gastos: src/gastos
Cada servicio tendrá sus propias rutas y funcionalidades específicas, que puedes explorar según tus necesidades.
