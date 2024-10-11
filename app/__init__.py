from flask import Flask
from app.config import Config
import mysql.connector
from mysql.connector import Error

# Inicializa la aplicación Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Conectar a la base de datos MySQL
    app.mysql_connection = create_mysql_connection(app.config)

    # Registro de rutas (controladores)
    from controllers.userController import bp as user_controller
    from controllers.clotheController import bp as clothe_controller
    from controllers.paymentTypeController import bp as paymentType_controller
    from controllers.billController import bp as bill_controller
    from controllers.shippingController import bp as shipping_controller

    app.register_blueprint(user_controller)
    app.register_blueprint(clothe_controller)
    app.register_blueprint(paymentType_controller)
    app.register_blueprint(bill_controller)
    app.register_blueprint(shipping_controller)

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
