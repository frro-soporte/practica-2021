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

''' @app.route('/create-socio')
def create_socio():
    return render_template('create.html') '''

''' @app.route('/save-socio', methods=['POST'])
def save_socio():
    socio = Socio(nombre=request.form['nombre'], pais=request.form['pais'])
    db.session.add(socio)
    db.session.commit()
    return 'Guardado'

@app.route('/eliminar-socio/<id>')
def delete(id):
    #socio = socio.query.filter_by(id=int(id)).first()
    Socio.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(request.referrer) '''

#Para editar se le le asigna por ej socio.nombre = request.form['nombre'] y después db.session.commit() y listo


if __name__ == '__main__':
    app.run(debug=True)
    #el debug es para poder ver los cambios sin reiniciar el sv.
