import csv, os
ruta_archivo_usuarios='modelos\\usuarios.csv'
usuarios=[]
id_usuario=1

def inicializar_usuarios():
    if os.path.exists(ruta_archivo_usuarios):
        importar_datos_desde_csv()

def exportar_a_csv():
    """
    Exporta los datos de usuarios a un archivo CSV.
    """
    with open(ruta_archivo_usuarios, 'w', newline='') as csvfile:
        campo_nombres = ["id_usuario", "nombre", "correo", "fecha_registro"]
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for user in usuarios:
            writer.writerow(user)

def importar_datos_desde_csv():
    """
    Importa los datos de usuarios desde un archivo CSV.
    """
    global usuarios
    global id_usuario
    usuarios = []  
    with open(ruta_archivo_usuarios, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            
            row['id_usuario'] = int(row['id_usuario'])
            usuarios.append(row) 
    if len(usuarios)>0:
        id_usuario= usuarios[-1]["id_usuario"]+1
    else:
        id_usuario = 1