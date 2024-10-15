from flask import current_app
from decimal import Decimal
from app.models.clothes import Clothes

def create_clothe(data):
    try:
        clothes = Clothes(
            id=None,
            marca=data['marca'],
            talla=data['talla'],
            cantidad_disponible=Decimal(data['cantidad_disponible']),
            colores=data['colores'],
            descripcion=data['descripcion'],
            tipo_prenda=data['tipo_prenda'],
            puntaje=data['puntaje'],
            comentario=data['comentario']   
        )

        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar una prenda
        insert_query = """INSERT INTO prendas
                          (marca, talla, cantidad_disponible, colores, descripcion, tipo_prenda, puntaje, comentario) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (clothes.marca, clothes.cantidad_disponible, clothes.colores, clothes.descripcion, clothes.tipo_prenda, clothes.puntaje, clothes.comentario))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'Prenda creada exitosamente'}, 201
    except Exception as e:
        print(f"Error al crear la prenda: {e}")
        return {'message': 'Error al crear la prenda'}, 500
    
def get_clothes():
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para seleccionar todas las prendas
        select_query = "SELECT * FROM prendas"
        cursor.execute(select_query)

        # Obtener todos los resultados
        clothes = cursor.fetchall()

        # Procesar los resultados
        clothes_list = []
        for row in clothes:
            clothes_list.append({
                'id': row[0],                  
                'marca': row[1],             
                'talla': row[2],           
                'cantidad_disponible': row[3],             
                'colores': row[4],    
                'descripcion': row[5],       
                'tipo_prenda': row[6],          
                'puntaje': row[7],
                'comentario' : row[8],
                'imagen': row[9],
                'valor' : row[10]
            })

        cursor.close()  # Cierra el cursor

        return clothes_list, 200 # Devuelve la lista de prendas

    except Exception as e:
        print(f"Error al obtener las prendas: {e}")
        return {'message': 'Error al obtener las prendas'}, 500