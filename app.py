from flask import Flask
from rutas.rutas_usuarios import usuarios_bp


from modelos.publicaciones import inicializar_publicaciones
from modelos.usuarios import inicializar_usuarios

app = Flask(__name__)

inicializar_publicaciones()
inicializar_usuarios()

app.register_blueprint(usuarios_bp)


if __name__ == '__main__':
    app.run(debug=True)