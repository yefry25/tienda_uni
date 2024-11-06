from app import get_db_connection

def CreateOrder(data):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        result, statusCode = GetOrderByUserId(data['UserId'])
        if result == None:
            
            # Llamada al procedimiento almacenado para crear la orden y agregar el primer item
            procedure_query = "CALL CrearOrdenConItem(%s, %s, %s)"
            
            # Ejecutar el procedimiento almacenado con los parámetros correspondientes
            cursor.execute(procedure_query, (data['UserId'], data['ProductId'], data['Amount']))

            connection.commit()  # Guarda los cambios
            cursor.close()

            return {'message': 'Orden creada exitosamente'}, 201
        else:

            OrderId = result['id']

            # Llamada al procedimiento almacenado para actualizar la orden y agregar el primer item
            procedure_query = "CALL ActualizarOrdenConItem(%s, %s, %s)"
            
            # Ejecutar el procedimiento almacenado con los parámetros correspondientes
            cursor.execute(procedure_query, (OrderId, data['ProductId'], data['Amount']))

            connection.commit()  # Guarda los cambios
            cursor.close()

            return {'message': 'Orden actualizada exitosamente'}, 201
        
    except Exception as e:
        print(f"Error al crear la orden: {e}")
        return {'message': 'Error al crear la orden'}, 500
    
    finally:
        if cursor:
            cursor.close()
  
def get_orders():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Consulta SQL para seleccionar todas las ordenes
        select_query = "SELECT * FROM Orden"
        cursor.execute(select_query)

        # Obtener todos los resultados
        orders = cursor.fetchall()

        # Procesar los resultados
        orders_list = []
        for row in orders:
            orders_list.append({
                'Id': row[0],                  
                'IdUsuario': row[1],             
                'IdPrenda': row[2],           
                'FechaCreacion': row[3]
            })

        cursor.close()  # Cierra el cursor

        return orders_list, 200

    except Exception as e:
        print(f"Error al obtener las ordenes: {e}")
        return {'message': 'Error al obtener las ordenes'}, 500
    
    finally:
        if cursor:
            cursor.close()

def GetOrderByUserId(userId: int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary = True)

        select_query = """
        SELECT * FROM ordenes
        WHERE idUsuario = %s AND
        idEstado = 2
        """
        cursor.execute(select_query, (userId,))

        # Obtener el resultado
        order = cursor.fetchone()
        return order, 200

    except Exception as e:
        print(f"Error al obtener el detalle de la orden: {e}")
        return {'message': 'Error al obtener el detalle de la orden'}, 500
    
    finally:
        if cursor:
            cursor.close()

def getOrderDetailByUserId(idUsuario: int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Consulta SQL para seleccionar las órdenes junto con la información de la prenda
        select_query = """
        SELECT
            orden.id AS idOrden,
            producto.id AS idProducto, 
            producto.nombre AS nombreProducto, 
            producto.descripcion AS descripcionProducto, 
            item.cantidad AS cantidadProducto,
            (SELECT GROUP_CONCAT(imagen.url SEPARATOR ', ') 
            FROM imagenes_producto imagen 
            WHERE imagen.idProducto = producto.id) AS imagen,
            SUM(item.subtotal) AS subTotal,
            orden.total
        FROM ordenes orden
        JOIN items_orden item ON orden.id = item.idOrden
        JOIN productos producto ON item.idProducto = producto.id
        WHERE orden.idUsuario = %s AND orden.idEstado = 2
        GROUP BY producto.id, producto.nombre, producto.descripcion, orden.total
        """
        cursor.execute(select_query, (idUsuario,))

        # Obtener todos los resultados
        orders = cursor.fetchall()

        # Procesar los resultados
        orders_list = []
        for row in orders:
            orders_list.append({
                'OrderId': row[0],                  
                'ProductId': row[1],             
                'ProductName': row[2],           
                'ProductDescription': row[3],
                'productAmount': row[4],
                'Imagen': row[5],
                'SubTotal': row[6],
                'Total': row[7]
            })

        cursor.close()  # Cierra el cursor

        return orders_list, 200

    except Exception as e:
        print(f"Error al obtener las ordenes: {e}")
        return {'message': 'Error al obtener las ordenes'}, 500
    
    finally:
        if cursor:
            cursor.close()
    
def UpdateOrder(orderId: int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Orden"
        cursor.execute(select_query)

        # Obtener todos los resultados
        orders = cursor.fetchall()

        TimeoutError
    except Exception as e:
        print(f"Error al crear la orden: {e}")
        return {'message': 'Error al crear la orden'}, 500
    
    finally:
        if cursor:
            cursor.close()