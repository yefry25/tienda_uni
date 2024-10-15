from flask import current_app
from decimal import Decimal
from app.models.shipping import Shipping

def create_shipping(data):
    try:
        shipping = Shipping(
            id=None,
            fecha_registro=data['fecha_registro'],
            prenda_id=data['prenda_id'],
            usuario_id=data['usuario_id'],
            direccion=data['direccion'],
            fecha_despacho = data['fecha_despacho'],
            fecha_estimada_llegada = data['fecha_estimada_llegada']
        )

        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar un envio
        insert_query = """INSERT INTO envios
                          (fecha_registro, prenda_id, usuario_id, direccion, fecha_despacho, fecha_estimada_llegada) 
                          VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (shipping.fecha_registro, shipping.prenda_id, shipping.usuario_id, shipping.direccion, shipping.fecha_despacho, shipping.fecha_estimada_llegada))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'Envío creada exitosamente'}, 201
    except Exception as e:
        print(f"Error al crear el envío: {e}")
        return {'message': 'Error al crear el envío'}, 500
    
def get_shippings():
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para seleccionar todos los envíos
        select_query = "SELECT * FROM envios"
        cursor.execute(select_query)

        # Obtener todos los resultados
        shippings = cursor.fetchall()

        # Procesar los resultados
        shippings_list = []
        for row in shippings:
            shippings_list.append({
                'id': row[0],                  
                'fecha_registro': row[1],             
                'prenda_id': row[2],           
                'usuario_id': row[3],             
                'direccion': row[4],    
                'fecha_despacho': row[5],       
                'fecha_estimada_llegada': row[6]
            })

        cursor.close()  # Cierra el cursor

        return {'shippings': shippings_list}, 200  # Devuelve la lista de envíos

    except Exception as e:
        print(f"Error al obtener las facturas: {e}")
        return {'message': 'Error al obtener las facturas'}, 500