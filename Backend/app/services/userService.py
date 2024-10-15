from flask import current_app
from datetime import datetime
from decimal import Decimal
from app.models.user import User  # Asegúrate de importar tu clase

# Servicio para crear un nuevo usuario en la base de datos
def create_user(data):
    try:
        # Convertir los datos recibidos en un objeto User
        user = User(
            id=None,
            nombres=data['nombres'],
            apellidos=data['apellidos'],
            usuario=data['usuario'],
            fecha_nacimiento=datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d'),
            total_compras=Decimal(data['total_compras']),
            direccion=data['direccion'],
            numero_telefonico=data['numero_telefonico'],
            password=data['password'],
            estado=data['estado']   
        )

        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar un nuevo usuario
        insert_query = """INSERT INTO usuarios
                          (nombres, apellidos, usuario, fecha_nacimiento, total_compras, direccion, numero_telefonico, password, estado) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (user.nombres, user.apellidos, user.usuario, user.fecha_nacimiento, user.total_compras, user.direccion, user.numero_telefonico, user.password, user.estado))

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
        select_query = "SELECT * FROM usuarios"
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
                'correo': row[4],          
                'fecha_nacimiento': row[5],    
                'total_compras': row[6],       
                'direccion': row[7],          
                'numero_telefonico': row[8],
                'password' : row[9],
                'estado' : row[10]
            })

        cursor.close()  # Cierra el cursor

        return {'users': user_list}  # Devuelve la lista de usuarios

    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return {'message': 'Error al obtener los usuarios'}
    
def update_user(user_id, data):
    try:
        if not user_id:
            return {'message': 'El ID de usuario es requerido'}, 400

        # Inicializa la consulta de actualización y los parámetros
        update_query = "UPDATE users SET "
        update_fields = []
        update_values = []

        # Chequea cada campo y lo agrega solo si está presente en 'data'
        if 'nombres' in data and data['nombres']:
            update_fields.append("nombres = %s")
            update_values.append(data['nombres'])

        if 'apellidos' in data and data['apellidos']:
            update_fields.append("apellidos = %s")
            update_values.append(data['apellidos'])

        if 'usuario' in data and data['usuario']:
            update_fields.append("usuario = %s")
            update_values.append(data['usuario'])

        if 'fecha_nacimiento' in data and data['fecha_nacimiento']:
            update_fields.append("fecha_nacimiento = %s")
            update_values.append(datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d'))

        if 'total_compras' in data and data['total_compras']:
            update_fields.append("total_compras = %s")
            update_values.append(Decimal(data['total_compras']))

        if 'direccion' in data and data['direccion']:
            update_fields.append("direccion = %s")
            update_values.append(data['direccion'])

        if 'numero_telefonico' in data and data['numero_telefonico']:
            update_fields.append("numero_telefonico = %s")
            update_values.append(data['numero_telefonico'])

        if 'password' in data and data['password']:
            update_fields.append("password = %s")
            update_values.append(data['password'])

        if 'estado' in data and data['estado']:
            update_fields.append("estado = %s")
            update_values.append(data['estado'])

        # Si no hay campos para actualizar, retornar un mensaje
        if not update_fields:
            return {'message': 'No hay campos para actualizar'}

        # Completa la consulta SQL
        update_query += ", ".join(update_fields) + " WHERE id = %s"
        update_values.append(user_id)

        # Ejecuta la consulta
        connection = current_app.mysql_connection
        cursor = connection.cursor()
        cursor.execute(update_query, update_values)
        connection.commit()

        return {'message': 'Usuario actualizado exitosamente'}, 201

    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return {'message': 'Error al actualizar el usuario'}, 500
    
def login(userName: str, password: str):
    try:
        # Conexión a la base de datos
        connection = current_app.mysql_connection
        cursor = connection.cursor(dictionary=True)

        # Consulta SQL para seleccionar el usuario por nombre de usuario
        select_query = "SELECT * FROM usuarios WHERE usuario = %s"
        cursor.execute(select_query, (userName,))
        
        # Obtener el usuario
        user = cursor.fetchone()  # Solo necesitamos un resultado

        if user:
            # Verificar la contraseña ingresada con la almacenada en la base de datos
            stored_password = user['password']  # Asegúrate de que la columna tenga el nombre correcto
            if stored_password == password:
                # La contraseña es correcta
                return user, 200
            else:
                # La contraseña es incorrecta
                return {'message': 'Usuario o contraseña incorrectos'}, 404
        else:
            # Usuario no encontrado
            return {'message': 'Usuario o contraseña incorrectos'}, 404

    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return {'message': 'Error al iniciar sesión'}, 500
