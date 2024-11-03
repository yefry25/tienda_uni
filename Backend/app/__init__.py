from flask import Flask
from app.config import Config
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS  # Importa CORS

# Inicializa la aplicación Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Habilitar CORS en toda la aplicación
    CORS(app)

    # Conectar a la base de datos MySQL
    app.mysql_connection = create_mysql_connection(app.config)

    # Registro de rutas (controladores)
    from app.Controllers.UserController import bp as UserController
    from app.Controllers.ProductController import bp as ProductController
    from app.Controllers.paymentTypeController import bp as paymentType_controller
    from app.Controllers.billController import bp as bill_controller
    from app.Controllers.shippingController import bp as shipping_controller
    from app.Controllers.OrderController import bp as OrderController

    app.register_blueprint(UserController)
    app.register_blueprint(ProductController)
    app.register_blueprint(paymentType_controller)
    app.register_blueprint(bill_controller)
    app.register_blueprint(shipping_controller)
    app.register_blueprint(OrderController)

    return app

# Crear una conexión a MySQL
def create_mysql_connection(config):
    try:
        connection = mysql.connector.connect(
            host=config['MYSQL_HOST'],
            database=config['MYSQL_DATABASE'],
            user=config['MYSQL_USER'],
            password=config['MYSQL_PASSWORD']
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return connection

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Cerrar la conexión a MySQL al terminar
def close_mysql_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Conexión a MySQL cerrada")
