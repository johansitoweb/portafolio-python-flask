from flask import Flask
from flask import render_template
from flask import send_from_directory


app = Flask(__name__)
@app.route("/")
def index():
    
    return render_template('sitio/index.html')

#la ruta de la imagen
# Ruta para mostrar la imagen
@app.route('/imagen')
def mostrar_imagen():
    # Especifica la carpeta 'static' donde se encuentra la imagen
    return send_from_directory('static', 'yigi.png', 'python.png')


if __name__ == "__main__":
    app.run(debug= True)

   #Este es un portafolio en el cual comparto toda mi informacion relacionada con cada cosas de la que e realizado en mi trancurso como desarollador
   # if
   

  