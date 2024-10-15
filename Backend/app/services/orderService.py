from flask import current_app
from app.models.order import Order

def create_order(data):
    try:
        order = Order(
        IdUsuario=data['idUsuario'],
        IdPrenda=data['idPrenda'],
        )

        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar una factura
        insert_query = """INSERT INTO orden
                          (IdUsuario, IdPrenda) 
                          VALUES (%s, %s)"""
        cursor.execute(insert_query, (order.IdUsuario, order.IdPrenda))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'Orden creada exitosamente'}, 201
    except Exception as e:
        print(f"Error al crear la orden: {e}")
        return {'message': 'Error al crear la orden'}, 500
    
def get_orders():
    try:
        connection = current_app.mysql_connection
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
    
def getOrderDetailByUserId(idUsuario: int):
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para seleccionar las órdenes junto con la información de la prenda
        select_query = """
            SELECT o.Id AS IdOrden, 
            o.IdUsuario,
            o.IdPrenda, 
            prenda.marca,
            prenda.valor,
            prenda.imagen,
            o.FechaCreacion
            FROM orden o
            JOIN prendas prenda ON o.IdPrenda = prenda.Id
            WHERE o.IdUsuario = %s
        """
        cursor.execute(select_query, (idUsuario,))

        # Obtener todos los resultados
        orders = cursor.fetchall()

        # Procesar los resultados
        orders_list = []
        for row in orders:
            orders_list.append({
                'IdOrden': row[0],                  
                'IdUsuario': row[1],             
                'IdPrenda': row[2],           
                'Marca': row[3],
                'Valor': row[4],
                'Imagen': row[5],
                'FechaCreacion': row[6]
            })

        cursor.close()  # Cierra el cursor

        return orders_list, 200

    except Exception as e:
        print(f"Error al obtener las ordenes: {e}")
        return {'message': 'Error al obtener las ordenes'}, 500