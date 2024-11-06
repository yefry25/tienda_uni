from app import get_db_connection

def SaleByProduct():
    try:
        connection = get_db_connection()
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

        result = {
            'items': saleList,
            'columns': [
                {'header': 'Producto', 'field': 'Product'},
                {'header': 'Cantidad Vendida', 'field': 'AmountSold'},
                {'header': 'Ingresos Totales', 'field': 'TotalIncome'}
            ]
        }

        return result, 200 # Devuelve la lista de productos vendidos
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
        return {'message': 'Error al obtener los productos'}, 500
    
    finally:
        if cursor:
            cursor.close()

def SaleByCategory():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        selected_query = """
        SELECT 
            cp.categoria AS Categoria,
            SUM(io.cantidad) AS CantidadVendida,
            SUM(io.subtotal) AS IngresosTotales
        FROM 
            productos p
        JOIN 
            categoria_productos cp ON p.idCategoria = cp.id
        JOIN 
            items_orden io ON p.id = io.idProducto
        JOIN 
            ordenes o ON io.idOrden = o.id
        WHERE
            o.idEstado = 1
        GROUP BY 
            cp.id
        ORDER BY 
            IngresosTotales DESC;
        """

        cursor.execute(selected_query);

        # Obtener todos los resultados
        sales = cursor.fetchall()

        # Procesar los resultados
        saleList = []
        for row in sales:
            saleList.append({
                'Category': row[0],                  
                'AmountSold': row[1],             
                'TotalIncome': row[2]
            })

        cursor.close()  # Cierra el cursor

        result = {
            'items': saleList,
            'columns': [
                {'header': 'Categoría', 'field': 'Category'},
                {'header': 'Cantidad Vendida', 'field': 'AmountSold'},
                {'header': 'Ingresos Totales', 'field': 'TotalIncome'}
            ]
        }

        return result, 200 # Devuelve la lista de productos vendidos

    except Exception as e:
        print(f"Error al obtener los productos por categoria: {e}")
        return {'message': 'Error al obtener los productos por categoria'}, 500
    
    finally:
        if cursor:
            cursor.close()

def StatusOfUsers():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        selected_query = """
        SELECT 
            activo AS Estado,
            COUNT(*) AS TotalClientes
        FROM 
            usuarios
        GROUP BY 
            activo;
        """

        cursor.execute(selected_query);

        # Obtener todos los resultados
        userStatus = cursor.fetchall()

            # Procesar los resultados
        userStatusList = []
        for row in userStatus:
            userStatusList.append({
                'Status': row[0],                  
                'UserTotal': row[1]
            })

        cursor.close()  # Cierra el cursor

        result = {
            'items': userStatusList,
            'columns':[
                {'header': 'Estado', 'field': 'Status'},
                {'header': 'Total de usuarios', 'field': 'UserTotal'}
            ]
        }

        return result, 200

    except Exception as e:
        print(f"Error al obtener el estado de los usuarios: {e}")
        return {'message': 'Error al obtener el estado de los usuarios'}, 500
    
    finally:
        if cursor:
            cursor.close()

def SalesForUsers():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        selected_query = """
        SELECT 
            u.nick AS Usuario,
            COUNT(o.id) AS NumeroDeOrdenes,
            SUM(o.total) AS TotalGastado
        FROM 
            usuarios u
        JOIN 
            ordenes o ON u.id = o.idUsuario
        GROUP BY 
            u.id
        ORDER BY 
            TotalGastado DESC;
        """

        cursor.execute(selected_query);

        # Obtener todos los resultados
        sales = cursor.fetchall()

        # Procesar los resultados
        saleList = []
        for row in sales:
            saleList.append({
                'NickName': row[0],                  
                'OrderNumber': row[1],             
                'SpendTotal': row[2]
            })

        cursor.close()  # Cierra el cursor

        result = {
            'items': saleList,
            'columns':[
                {'header': 'Usuario', 'field': 'NickName'},
                {'header': 'Número de orden', 'field': 'OrderNumber'},
                {'header': 'Total gastado', 'field': 'SpendTotal'}
            ]
        }

        return result, 200

    except Exception as e:
        print(f"Error: {e}")
        return {'message': 'Error al obtener el total gastado por usuarios'}, 500
    
    finally:
        if cursor:
            cursor.close()

def ProductInventory():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        selected_query = """
        SELECT 
            nombre AS Producto,
            stock AS Inventario
        FROM 
            productos
        ORDER BY 
            stock ASC;
        """

        cursor.execute(selected_query);

        # Obtener todos los resultados
        products = cursor.fetchall()

        # Procesar los resultados
        productList = []
        for row in products:
            productList.append({
                'Product': row[0],                  
                'Inventary': row[1]
            })

        cursor.close()  # Cierra el cursor

        result = {
            'items': productList,
            'columns':[
                {'header': 'Producto', 'field': 'Product'},
                {'header': 'Inventario', 'field': 'Inventary'}
            ]
        }

        return result, 200

    except Exception as e:
        print(f"Error: {e}")
        return {'message': 'Error al obtener el inventario de los productos'}, 500
    
    finally:
        if cursor:
            cursor.close()

def OrderStatus():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        selected_query = """
        SELECT 
            eo.estado AS Estado,
            COUNT(o.id) AS NumeroDeOrdenes
        FROM 
            ordenes o
        JOIN 
            estado_orden eo ON o.idEstado = eo.id
        GROUP BY 
            eo.id;
        """

        cursor.execute(selected_query);

        # Obtener todos los resultados
        orders = cursor.fetchall()

        # Procesar los resultados
        orderList = []
        for row in orders:
            orderList.append({
                'Status': row[0],                  
                'OrderNumber': row[1]
            })

        cursor.close()  # Cierra el cursor

        result = {
            'items': orderList,
            'columns':[
                {'header': 'Estado', 'field': 'Status'},
                {'header': 'Número de orden', 'field': 'OrderNumber'}
            ]
        }

        return result, 200

    except Exception as e:
        print(f"Error: {e}")
        return {'message': 'Error al obtener el estado de las ordenes'}, 500
    
    finally:
        if cursor:
            cursor.close()

def IssuedBills():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        selected_query = """
        SELECT 
            f.id AS NumeroFactura,
            u.nick AS Cliente,
            f.fechaEmision AS FechaDeEmision,
            o.total AS Total
        FROM 
            facturas f
        JOIN 
            usuarios u ON f.idUsuario = u.id
        JOIN 
            ordenes o ON f.idOrden = o.id
        ORDER BY 
            f.fechaEmision DESC;
        """

        cursor.execute(selected_query);

        # Obtener todos los resultados
        bills = cursor.fetchall()

        # Procesar los resultados
        billList = []
        for row in bills:
            billList.append({
                'BillId': row[0],                  
                'NickName': row[1],
                'IssuedDate': row[2],
                'Total': row[3]
            })

        cursor.close()  # Cierra el cursor

        result = {
            'items': billList,
            'columns':[
                {'header': 'Id de factura', 'field': 'BillId'},
                {'header': 'Usuario', 'field': 'NickName'},
                {'header': 'Fecha emision', 'field': 'IssuedDate'},
                {'header': 'Total', 'field': 'Total'}
            ]
        }

        return result, 200

    except Exception as e:
        print(f"Error: {e}")
        return {'message': 'Error al obtener las facturas por usuario'}, 500
    
    finally:
        if cursor:
            cursor.close()

def MonthlyIncome():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        selected_query = """
        SELECT 
            DATE_FORMAT(o.fechaCreacion, '%Y-%m') AS Mes,
            SUM(o.total) AS IngresosTotales
        FROM 
            ordenes o
        GROUP BY 
            DATE_FORMAT(o.fechaCreacion, '%Y-%m')
        ORDER BY 
            Mes DESC;
        """

        cursor.execute(selected_query);

        # Obtener todos los resultados
        incomes = cursor.fetchall()

        # Procesar los resultados
        incomeList = []
        for row in incomes:
            incomeList.append({
                'Month': row[0],                  
                'TotalIncome': row[1]
            })

        cursor.close()  # Cierra el cursor

        result = {
            'items': incomeList,
            'columns':[
                {'header': 'Mes', 'field': 'Month'},
                {'header': 'Ingresos Totales', 'field': 'TotalIncome'}
            ]
        }

        return result, 200

    except Exception as e:
        print(f"Error: {e}")
        return {'message': 'Error al obtener los ingresos'}, 500
    
    finally:
        if cursor:
            cursor.close()