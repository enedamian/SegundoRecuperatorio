from flask import Blueprint, jsonify, request
from modelos.publicaciones import obtener_publicaciones, obtener_publicacion_por_id, crear_publicacion, editar_publicacion_por_id

publicaciones_bp = Blueprint('publicaciones_bp', __name__)


@publicaciones_bp.route('/publicaciones/<int:id>', methods=['GET'])
def buscar_publicacion_id(id):
    publicacion = obtener_publicacion_por_id(id)
    if publicacion:
        return jsonify(publicacion), 200
    else:
        return jsonify({'error': 'Publicacion no encontrada'}), 200
    
@publicaciones_bp.route('/publicaciones', methods=['POST'])
def nueva_publicacion():
    if request.is_json:
        nuevo = request.get_json()
        publicacion = crear_publicacion(nuevo['id_usuario'], nuevo['contenido'], nuevo['fecha_publicacion'])
        return jsonify(publicacion), 201
        
    else:
        return jsonify({'error': 'No se recibió el formato JSON'}), 200
    
@publicaciones_bp.route('/publicaciones', methods=['PUT'])
def editar_libro_id(id):
    if request.is_json:
        nuevo = request.get_json() 
        publicacion = editar_publicacion_por_id(id, nuevo['id_usuario'], nuevo['contenido'], nuevo['fecha_publicacion'])
        if publicacion:
            return jsonify(publicacion), 200
        else:
            return jsonify({'error': 'Publicacion no encontrada'}), 200
    else:
        return jsonify({'error': 'No se recibió el formato JSON'}), 200