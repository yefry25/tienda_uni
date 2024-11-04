from flask import current_app

def CreateBill(data):
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar una factura
        insert_query = "CALL CrearFactura(%s, %s)"
        cursor.execute(insert_query, (data['OrderId'], data['UserId']))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'Factura creada exitosamente'}, 201
    except Exception as e:
        print(f"Error al crear la factura: {e}")
        return {'message': 'Error al crear la factura'}, 500
    
def get_bills():
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para seleccionar todas las facturas
        select_query = "SELECT * FROM factura"
        cursor.execute(select_query)

        # Obtener todos los resultados
        bills = cursor.fetchall()

        # Procesar los resultados
        bill_list = []
        for row in bills:
            bill_list.append({
                'Id': row[0],                  
                'IdOrden' : row[1],
                'MontoTotal': row[2],
                'FechaEmision': row[3]
            })

        cursor.close()  # Cierra el cursor

        return bill_list, 200  # Devuelve la lista de facturas

    except Exception as e:
        print(f"Error al obtener las facturas: {e}")
        return {'message': 'Error al obtener las facturas'}, 500