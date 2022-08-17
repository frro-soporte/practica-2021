from flask import Flask, render_template, request, redirect, url_for
from ..practico_05.ejercicio_01 import Base, Socio
from ..practico_05.ejercicio_02 import DatosSocio
from ..practico_06.capa_negocio import NegocioSocio


app = Flask(__name__)
#Esto para crear las rutas

@app.route('/')
def home():
    socios = DatosSocio().todos()    
    return render_template('index.html', socios = socios)

@app.route('/create-socio')
def create_socio():
    return render_template('create.html')

@app.route('/save-socio', methods=['POST'])
def save_socio():
    socio = Socio(nombre=request.form['nombre'], apellido=request.form['apellido'], dni=request.form['dni'])
    DatosSocio().alta(socio)
    socios = DatosSocio().todos()    
    return redirect('/')

@app.route('/edit-socio/<id>')
def edit_socio(id):
    socio = DatosSocio().buscar(id)
    return render_template('edit.html', socio = socio)

@app.route('/update-socio/<id>', methods=['POST'])
def update(id):
    socio = DatosSocio().buscar(id)
    socio.nombre = request.form['nombre']
    socio.apellido = request.form['apellido']
    socio.dni = request.form['dni']
    DatosSocio().modificacion(socio)
    return redirect('/')

@app.route('/eliminar-socio/<id>')
def delete(id, methods=['DELETE']):
    DatosSocio().baja(id)
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(debug=True)
    #el debug es para poder ver los cambios sin reiniciar el sv.
