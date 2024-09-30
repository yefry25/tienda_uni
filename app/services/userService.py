from flask import current_app
from datetime import datetime
from decimal import Decimal
from app.models.user import User  # Asegúrate de importar tu clase

# Servicio para crear un nuevo usuario en la base de datos
def create_user(data):
    try:
        # Convertir los datos recibidos en un objeto User
        user = User(
            id=None,  # Asumimos que la base de datos genera el id automáticamente
            nombres=data['nombres'],
            apellidos=data['apellidos'],
            usuario=data['usuario'],
            fecha_nacimiento=datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d'),
            total_compras=Decimal(data['total_compras']),
            direccion=data['direccion'],
            numero_telefonico=data['numero_telefonico']
        )

        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar un nuevo usuario
        insert_query = """INSERT INTO usuarios
                          (nombres, apellidos, usuario, fecha_nacimiento, total_compras, direccion, numero_telefonico) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (user.nombres, user.apellidos, user.usuario, user.fecha_nacimiento, user.total_compras, user.direccion, user.numero_telefonico))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'Usuario creado exitosamente'}

    except Exception as e:
        print(f"Error al insertar usuario: {e}")
        return {'message': 'Error al crear el usuario'}

def get_users():
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para seleccionar todos los usuarios
        select_query = "SELECT * FROM usuarios"  # Asegúrate de que el nombre de la tabla sea correcto
        cursor.execute(select_query)

        # Obtener todos los resultados
        users = cursor.fetchall()

        # Procesar los resultados
        user_list = []
        for row in users:
            user_list.append({
                'id': row[0],                  
                'nombres': row[1],             
                'apellidos': row[2],           
                'usuario': row[3],             
                'fecha_nacimiento': row[4],    
                'total_compras': row[5],       
                'direccion': row[6],          
                'numero_telefonico': row[7]    
            })

        cursor.close()  # Cierra el cursor

        return {'users': user_list}  # Devuelve la lista de usuarios

    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return {'message': 'Error al obtener los usuarios'}
