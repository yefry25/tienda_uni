from app import get_db_connection

def CreateProduct(data):
    try:
        # Obtener la conexión a la base de datos
        connection = get_db_connection()
        cursor = connection.cursor()

        # Consulta SQL para insertar un producto
        insert_product_query = """
            INSERT INTO productos (nombre, idCategoria, idMarca, precio, stock, descripcion, activo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        product_values = (data['name'], data['categoryId'], data['brandId'], data['price'], data['stock'], data['description'], 1)
        cursor.execute(insert_product_query, product_values)

        # Obtener el ID del producto recién creado
        product_id = cursor.lastrowid

        # Consulta SQL para crear un espacio de imagen asociado al producto
        insert_image_query = """
            INSERT INTO imagenes_producto (idProducto, url) 
            VALUES (%s, %s)
        """
        # `url` inicialmente será un valor por defecto (por ejemplo, vacío o un marcador)
        image_values = (product_id, data['image'])
        cursor.execute(insert_image_query, image_values)

        # Confirmar los cambios en la base de datos
        connection.commit()

        return {'message': 'Producto creado exitosamente.'}, 201

    except Exception as e:
        # Registrar el error para depuración
        print(f"Error al crear el producto: {e}")
        return {'message': 'Error al crear el producto'}, 500

    finally:
        # Cerrar el cursor y la conexión de forma segura
        if cursor:
            cursor.close()

def UpdateProduct(id, data):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Consulta SQL para insertar un producto
        update_query = """UPDATE productos
                        SET nombre = %s,
                        idCategoria = %s,
                        idMarca = %s,
                        precio = %s,
                        stock = %s,
                        descripcion = %s,
                        activo = 1
                        WHERE id = %s"""
        cursor.execute(update_query, (data['name'], data['categoryId'], data['brandId'], data['price'], data['stock'], data['description'], id,))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'Producto editado exitosamente'}, 201
    except Exception as e:
        print(f"Error al editar el producto: {e}")
        return {'message': 'Error al editar el producto'}, 500
    
    finally:
        if cursor:
            cursor.close()

def DeleteProduct(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = """
        UPDATE productos
        SET activo = 0
        WHERE id = %s
        """

        # Convertimos id en una tupla pasando una coma después del valor
        cursor.execute(insert_query, (id,))
        connection.commit()

        return {'message': 'producto eliminado satisfactoriamente'}, 200

    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
        return {'message': 'Error al eliminar el producto'}, 500
    
    finally:
        if cursor:
            cursor.close()

def GetProducts():
    try:
        connection = get_db_connection()
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
        products = cursor.fetchall()

        # Procesar los resultados
        product_list = []
        for row in products:
            product_list.append({
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

        return product_list, 200 # Devuelve la lista de prendas

    except Exception as e:
        print(f"Error al obtener los productos: {e}")
        return {'message': 'Error al obtener los productos'}, 500
    
    finally:
        if cursor:
            cursor.close()

def GetProductById(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        select_query = """
        SELECT * FROM productos
        WHERE id = %s
        """

        cursor.execute(select_query, (id,))

        # Obtener todos los resultados
        product = cursor.fetchone()

        result= {
            'id': product['id'],
            'name': product['nombre'],
            'categoryId': product['idCategoria'],
            'brandId': product['idMarca'],
            'price': product['precio'],
            'stock': product['stock'],
            'description' : product['descripcion'],
            'active': product['activo']
        }

        cursor.close()

        return result, 200

    except Exception as e:
        print(f"Error al obtener el detalle del producto: {e}")
        return {'message': 'Error al obtener el detalle del producto'}, 500
    
    finally:
        if cursor:
            cursor.close()
