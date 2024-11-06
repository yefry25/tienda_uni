from flask import current_app

def CreateProduct(data):
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar un producto
        insert_query = """INSERT INTO productos
                          (nombre, idCategoria, idMarca, precio, stock, descripcion, activo) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (data['Name'], data['CategoryId'], data['BrandId'], data['Price'], data['Stock'], data['Description'], 1))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'Producto creada exitosamente'}, 201
    except Exception as e:
        print(f"Error al crear el producto: {e}")
        return {'message': 'Error al crear el producto'}, 500
    
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