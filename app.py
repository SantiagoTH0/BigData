from flask import Flask, render_template, url_for

app = Flask(__name__)

# Ruta principal: Inicio
@app.route('/')
def home():
    return render_template('index.html')

# Rutas CRISP-DM
@app.route('/crisp-dm/negocio')
def crisp_negocio():
    return render_template('crisp_negocio.html')

@app.route('/crisp-dm/datos')
def crisp_datos():
    return render_template('crisp_datos.html')

@app.route('/crisp-dm/preparacion')
def crisp_preparacion():
    return render_template('crisp_preparacion.html')

@app.route('/crisp-dm/evaluacion')
def crisp_evaluacion():
    return render_template('crisp_evaluacion.html')

# Tablero Power BI
@app.route('/tablero')
def tablero():
    return render_template('tablero.html')

if __name__ == '__main__':
    app.run(debug=True)