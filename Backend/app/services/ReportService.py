from flask import current_app

def SaleByProduct():
    try:
        connection = current_app.mysql_connection
        cursor = connection.cursor()

        # Consulta SQL para seleccionar todas las facturas
        select_query = """
        SELECT 
            p.nombre AS Producto,
            SUM(io.cantidad) AS CantidadVendida,
            SUM(io.subtotal) AS IngresosTotales
        FROM 
            productos p
        JOIN 
            items_orden io ON p.id = io.idProducto
        JOIN 
            ordenes o ON io.idOrden = o.id
        WHERE 
            o.idEstado = 1
        GROUP BY
            p.id
        ORDER BY
            IngresosTotales DESC;
        """
        cursor.execute(select_query)

        # Obtener todos los resultados
        sales = cursor.fetchall()

        # Procesar los resultados
        saleList = []
        for row in sales:
            saleList.append({
                'Product': row[0],                  
                'AmountSold': row[1],             
                'TotalIncome': row[2]
            })

        cursor.close()  # Cierra el cursor

        return saleList, 200 # Devuelve la lista de prendas
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
        return {'message': 'Error al obtener los productos'}, 500