from flask import current_app
from decimal import Decimal
from models.paymentType import payment_type

def create_paymentType(data):
    try:
        paymentType = payment_type(
            id=None,
            tipo_pago=data['tipo_pago'],
            monto_pagado=data['monto_pagado'],
            usuario_id=data['usuario_id'],
            prenda_id=data['prenda_id']
        )

        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para insertar una prenda
        insert_query = """INSERT INTO metodos_pago
                          (tipo_pago, monto_pagado, usuario_id, prenda_id) 
                          VALUES (%s, %s, %s, %s)"""
        cursor.execute(insert_query, (paymentType.tipo_pago, paymentType.monto_pagado, paymentType.usuario_id, paymentType.prenda_id))

        connection.commit()  # Guarda los cambios
        cursor.close()

        return {'message': 'tipo pago creado exitosamente'}, 201
    except Exception as e:
        print(f"Error al crear el tipo pago: {e}")
        return {'message': 'Error al crear el tipo pago'}, 500