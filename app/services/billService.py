from flask import current_app
from decimal import Decimal
from models.bill import Bill

def create_bill(data):
    try:
        bill = Bill(
            id=None,
            fecha_compra=data['fecha_compra'],
            prenda_id=data['prenda_id'],
            precio=Decimal(data['precio']),
            referencia=data['referencia'],
            talla = data['talla'],
            iva = data['iva'],
            descuento = data['descuento'],
            total = data['total']
        )

        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar una factura
        insert_query = """INSERT INTO facturas
                          (fechaHora_compra, prenda_id, precio, referencia, talla, iva, descuento, total) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (bill.fecha_compra, bill.prenda_id, bill.precio, bill.referencia, bill.talla, bill.iva, bill.descuento, bill.total))

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
        select_query = "SELECT * FROM facturas"
        cursor.execute(select_query)

        # Obtener todos los resultados
        bills = cursor.fetchall()

        # Procesar los resultados
        clothes_list = []
        for row in bills:
            clothes_list.append({
                'id': row[0],                  
                'fechaHora_compra': row[1],             
                'prenda_id': row[2],           
                'precio': row[3],             
                'referencia': row[4],    
                'talla': row[5],       
                'iva': row[6],          
                'descuento': row[7],
                'total' : row[8]
            })

        cursor.close()  # Cierra el cursor

        return {'bills': clothes_list}, 200  # Devuelve la lista de facturas

    except Exception as e:
        print(f"Error al obtener las facturas: {e}")
        return {'message': 'Error al obtener las facturas'}, 500