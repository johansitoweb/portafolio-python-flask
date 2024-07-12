# from flask import Flask, send_from_directory

# app = Flask(__name__)

# # Ruta para mostrar la imagen
# @app.route('/imagen')
# def mostrar_imagen():
#     # Especifica la ruta de la carpeta donde se encuentra la imagen
#     return send_from_directory('ruta/a/tu/carpeta', 'nombre_de_tu_imagen.jpg')

# # Ruta principal
# @app.route('/')
# def inicio():
#     nombre = "hola mundo soy python"
#     return 'Hola, esta es mi página! <img src="/imagen" alt="imagen">'

# if __name__ == '__main__':
#     app.run()