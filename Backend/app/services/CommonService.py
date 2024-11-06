from app import get_db_connection

def GetCategories():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(buffered=True)

        selected_query= """
        SELECT * FROM categoria_productos
        """

        cursor.execute(selected_query)
        categories = cursor.fetchall()

        # Procesar los resultados
        categoriesList = []
        for row in categories:
            categoriesList.append({
                'Id': row[0],                  
                'Name' : row[1]
            })

        return categoriesList, 200

    except Exception as e:
        print(f"Error al listar categorias: {e}")
        return {'message': 'Error al listar categorias'}, 500
    
    finally:
        if cursor:
            cursor.close()
    
def GetBrands():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(buffered=True)

        selected_query= """
        SELECT * FROM marcas
        """

        cursor.execute(selected_query)
        brands = cursor.fetchall()

        # Procesar los resultados
        brandList = []
        for row in brands:
            brandList.append({
                'Id': row[0],                  
                'Name' : row[1]
            })

        return brandList, 200

    except Exception as e:
        print(f"Error al listar marcas: {e}")
        return {'message': 'Error al listar marcas'}, 500
    
    finally:
        if cursor:
            cursor.close()
