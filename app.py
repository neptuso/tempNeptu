from flask import Flask, render_template

from scraper import obtener_datos_meteorologicos

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://chajarialdia.com.ar/estacion/index.html'
    datos = obtener_datos_meteorologicos(url)
    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
