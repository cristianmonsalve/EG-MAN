from flask import Flask, render_template, request
import requests
from flask_cors import CORS


app = Flask(__name__, template_folder='templates', static_folder='static' )

@app.route('/listarCentral', methods=['GET'])
def listarCentral():
    centrales = requests.get('http://localhost:4000/central').json()
    return render_template('index.html', centrales=centrales)


@app.route('/crearCentrales', methods=['GET'])
def crearCentrales():
    return render_template('crearCentral.html')


@app.route('/guardarCentrales', methods=['POST'])
def guardarCentrales():

    central = dict(request.values)
    
    central['origen'] = str(request.form['origen'])
    central['destinatario'] = str(request.form['destinatario'])
    central['estado_conexion'] = str(request.form['estado_conexion'])
    central['estado_actual'] = str(request.form['estado_actual'])
    central['fecha'] = str(request.form['fecha'])

    requests.post('http://localhost:4000/central', json=central)

    return (listarCentral())


app.run(port=4002, host='0.0.0.0', debug=True)