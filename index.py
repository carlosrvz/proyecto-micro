# Se importa el objeto Flask desde el paquete flask
from flask import Flask, render_template, send_file

app = Flask(__name__)       # Se crea una instancia de aplicación Flask con el nombre app

@app.route('/')             # Se define la ruta a la que podrá acceder la app
def home():
    return render_template('home.html') # Renderiza y usa la plantilla home.html

@app.route('/download')     # Se define otra ruta a la que podrá acceder la app
def download():
    p = "data.txt"          # En este caso para descargar los datos que nos de el microcontrolador
    return send_file(p,as_attachment=True)  # La función send_file() devuelve el contenido del fichero

if __name__ == '__main__':
    app.run(debug = True)       # Se activa la depuración
