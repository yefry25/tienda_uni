import os

class Config:
    # Configuración de la base de datos MySQL
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'tienda')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')