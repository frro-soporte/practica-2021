from flask import Flask, render_template, request, redirect, url_for
from practico_05.ejercicio_01 import Base, Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado

app = Flask(__name__)
#Esto para crear las rutas

@app.route('/')
def home():
    socios = NegocioSocio().todos()
    return render_template('index.html', socios = socios)

@app.route('/create-socio')
def create_socio():
    return render_template('create.html')

@app.route('/save-socio', methods=['POST'])
def save_socio():
    socio = Socio(nombre=request.form['nombre'], apellido=request.form['apellido'], dni=request.form['dni'])
    try:
        NegocioSocio().alta(socio)
    except LongitudInvalida as e:
        return render_template('/error1.html', id_socio = 'void')
    except DniRepetido as e:
        return render_template('/error2.html')
    except MaximoAlcanzado as e:
        return render_template('/error3.html')
    socios = NegocioSocio().todos()
    return redirect('/')

@app.route('/edit-socio/<id>')
def edit_socio(id):
    socio = NegocioSocio().buscar(id)
    return render_template('edit.html', socio = socio)

@app.route('/update-socio/<id>', methods=['POST'])
def update(id):
    socio = NegocioSocio().buscar(id)
    socio.nombre = request.form['nombre']
    socio.apellido = request.form['apellido']
    socio.dni = request.form['dni']
    try:
        NegocioSocio().modificacion(socio)
    except LongitudInvalida as e:
        return render_template('error1.html', id_socio = socio.id)
    return redirect('/')

@app.route('/eliminar-socio/<id>')
def delete(id, methods=['DELETE']):
    NegocioSocio().baja(id)
    return redirect(request.referrer)


@app.route('/error1')
def error_1():
    return render_template('error1.html')


@app.route('/error2')
def error_2():
    return render_template('error2.html')


@app.route('/error3')
def error_3():
    return render_template('error3.html')


if __name__ == '__main__':
    app.run(debug=True)
    #el debug es para poder ver los cambios sin reiniciar el sv.
