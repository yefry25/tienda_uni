from flask import current_app
from decimal import Decimal
from app.Models.Product import Product

def create_clothe(data):
    try:
        clothes = Product(
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
    
def GetProducts():
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para seleccionar todas las prendas
        select_query = """
            SELECT 
                producto.id, 
                producto.nombre, 
                categoria.categoria, 
                marca.nombre AS marca, 
                producto.precio,
                producto.stock,
                producto.descripcion,
                GROUP_CONCAT(imagen.url SEPARATOR ', ') AS imagenes
            FROM 
                productos producto
            JOIN 
                imagenes_producto imagen ON producto.id = imagen.idProducto
            JOIN 
                categoria_productos categoria ON producto.idCategoria = categoria.id
            JOIN 
                marcas marca ON producto.idMarca = marca.id
            WHERE 
                producto.activo = 1
            GROUP BY 
                producto.id, producto.nombre, producto.stock, categoria.categoria, marca.nombre, producto.precio;
        """
    
        cursor.execute(select_query)

        # Obtener todos los resultados
        clothes = cursor.fetchall()

        # Procesar los resultados
        clothes_list = []
        for row in clothes:
            clothes_list.append({
                'id': row[0],                  
                'name': row[1],             
                'category': row[2],           
                'brand': row[3],             
                'price': row[4],    
                'stock': row[5],       
                'description': row[6],
                'images': row[7]
            })

        cursor.close()  # Cierra el cursor

        return clothes_list, 200 # Devuelve la lista de prendas

    except Exception as e:
        print(f"Error al obtener los productos: {e}")
        return {'message': 'Error al obtener los productos'}, 500