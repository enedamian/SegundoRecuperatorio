import os, csv

publicaciones = []
id_publicacion = 1  
ruta_archivo_publicaciones = 'modelos\\publicaciones.csv'

# estructura: id_publicacion, id_usuario, contenido, fecha_publicacion

def inicializar_publicaciones():
    """
    Inicializa la variable global id_publicacion y verifica si existe el archivo de datos de publicaciones.
    Si existe, importa los datos desde el archivo CSV correspondiente.
    """
    global id_publicacion
    if os.path.exists(ruta_archivo_publicaciones):
        importar_datos_desde_csv()

def crear_publicacion(id_usuario, contenido, fecha_publicacion):
    """
    Crea una nueva publicación con los datos proporcionados y la agrega a la lista de publicaciones.

    Args:
        id_usuario (int): El ID del usuario que realiza la publicación.
        contenido (str): El contenido de la publicación.
        fecha_publicacion (str): La fecha de publicación de la publicación.

    Returns:
        dict: Un diccionario que representa la publicación recién creada.
    """
    global id_publicacion
    publicaciones.append({
        "id_publicacion": id_publicacion,
        "id_usuario": id_usuario,
        "contenido": contenido,
        "fecha_publicacion": fecha_publicacion
    })
    id_publicacion += 1
    exportar_a_csv()
    return publicaciones[-1]

def obtener_publicacion_por_id(id_publicacion):
    """
    Devuelve la publicación con el ID especificado.

    Parámetros:
        id_publicacion (int): El ID de la publicación a buscar.

    Retorna:
        dict: El diccionario que representa la publicación encontrada, o None si no se encuentra.
    """
    for publicacion in publicaciones:
        if publicacion["id_publicacion"] == id_publicacion:
            return publicacion
    return None



def editar_publicacion_por_id(id_publicacion, id_usuario, contenido, fecha_publicacion):
    """
    Edita una publicación en la lista de publicaciones por su ID.

    Parámetros:
        id_publicacion (int): El ID de la publicación a editar.
        id_usuario (int): El nuevo ID del usuario de la publicación.
        contenido (str): El nuevo contenido de la publicación.
        fecha_publicacion (str): La nueva fecha de publicación de la publicación.

    Retorna:
        dict: El diccionario de la publicación editada.
        None: Si no se encuentra la publicación con el ID especificado.
    """
    for publicacion in publicaciones:
        if publicacion["id_publicacion"] == id_publicacion:
            publicacion["id_usuario"] = id_usuario
            publicacion["contenido"] = contenido
            publicacion["fecha_publicacion"] = fecha_publicacion
            exportar_a_csv()
            return publicacion
    return None



def existe_publicacion(id_publicacion):
    """
    Verifica si existe una publicación con el ID especificado en la lista de publicaciones.

    Args:
        id_publicacion (int): El ID de la publicación a buscar.

    Returns:
        bool: True si la publicación existe, False si no.
    """
    for publicacion in publicaciones:
        if publicacion["id_publicacion"] == id_publicacion:
            return True
    return False

def exportar_a_csv():
    """
    Exporta los datos de las publicaciones a un archivo CSV.
    """
    with open(ruta_archivo_publicaciones, 'w', newline='', encoding='utf8') as csvfile:
        campo_nombres = ['id_publicacion', 'id_usuario', 'contenido', 'fecha_publicacion']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for publicacion in publicaciones:
            writer.writerow(publicacion)

def importar_datos_desde_csv():
    """
    Importa los datos de las publicaciones desde un archivo CSV.
    """
    global publicaciones
    global id_publicacion
    publicaciones = []
    with open(ruta_archivo_publicaciones, newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id_publicacion'] = int(row['id_publicacion'])
            publicaciones.append(row) 
    if len(publicaciones) > 0:
        id_publicacion = publicaciones[-1]["id_publicacion"] + 1
    else:
        id_publicacion = 1