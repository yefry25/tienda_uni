from flask import Flask, g
from app.config import Config
import mysql.connector
from mysql.connector import pooling, Error
from flask_cors import CORS
from flask import current_app

# Inicializa la aplicación Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Habilitar CORS en toda la aplicación
    CORS(app)

    # Crear un pool de conexiones MySQL y asignarlo a app
    app.mysql_pool = create_mysql_pool(app.config)

    # Registro de rutas (controladores)
    from app.Controllers.UserController import bp as UserController
    from app.Controllers.ProductController import bp as ProductController
    from app.Controllers.BillController import bp as BillController
    from app.Controllers.OrderController import bp as OrderController
    from app.Controllers.ReportController import bp as ReportController
    from app.Controllers.CommonController import bp as CommonController

    app.register_blueprint(UserController)
    app.register_blueprint(ProductController)
    app.register_blueprint(BillController)
    app.register_blueprint(OrderController)
    app.register_blueprint(ReportController)
    app.register_blueprint(CommonController)

    # Cerrar conexión al terminar la solicitud
    @app.teardown_appcontext
    def close_db_connection(exception):
        db = g.pop('db', None)
        if db:
            db.close()
            print("Conexión a MySQL cerrada al finalizar la solicitud")

    return app

# Crear un pool de conexiones a MySQL
def create_mysql_pool(config):
    try:
        pool = pooling.MySQLConnectionPool(
            pool_name="mysql_pool",
            pool_size=5,
            host=config['MYSQL_HOST'],
            database=config['MYSQL_DATABASE'],
            user=config['MYSQL_USER'],
            password=config['MYSQL_PASSWORD']
        )
        print("Pool de conexiones MySQL creado exitosamente")
        return pool

    except Error as e:
        print(f"Error al crear el pool de conexiones MySQL: {e}")
        return None

# Obtener la conexión de la solicitud usando el pool
def get_db_connection():
    if 'db' not in g:
        g.db = current_app.mysql_pool.get_connection()
    return g.db
