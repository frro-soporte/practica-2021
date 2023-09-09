from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.location import location
from data.db import db
from flask_login import current_user, login_required

locations = Blueprint('locations', __name__)

@locations.route("/locations", methods=["GET"])
@login_required
def getAll():
    loc = location.query.all()
    return render_template('location/list.html',locs=loc)

@locations.route("/locations/<id>", methods=["GET"])
def getbyid(id):
    return location.query.get(id)

@locations.route("/location/create", methods=["POST", "GET"])
def create():
    if request.method == 'GET':
        return render_template('location/create.html')
    
    name = request.form['name']
    userId = current_user.id
    description = request.form['description']
    
    createrol = location.query.filter_by(name=name).first()
    if createrol :
        flash("Ya existe una ubicación con ese nombre","alert alert-danger")
        return redirect(url_for('locations.create'))

    if name == '':
        flash("Debe ingresar la ubicación.","alert alert-danger")
        return redirect(url_for('locations.create'))
    

    add = location(userId,name,description,1)

    db.session.add(add)
    db.session.commit()

    flash("La ubicación se guardo correctamente", "alert alert-success")

    return redirect(url_for('locations.getAll'))

@locations.route("/location/update/<id>", methods=["POST", "GET"])
def update(id):
    if request.method == 'POST':
        update = location.query.get(id)
        
        update.name = request.form['name']
        update.description = request.form['description']
        
        db.session.commit()

        flash("La ubicación se actualizo correctamente", "alert alert-success")

        return redirect(url_for('locations.getAll'))
    else:    
        updateid = location.query.get(id)
        return render_template('location/update.html', updates=updateid)

@locations.route("/location/delete/<id>")
def delete(id):
   try:
        dele = location.query.get(id)
        db.session.delete(dele)
        db.session.commit()
        
        flash("La ubicación se elimino correctamente", "alert alert-success")

        return redirect(url_for('locations.getAll'))
   except Exception as ex:
        flash("No se puede eliminar esta ubicación porque tiene kayak asociado","alert alert-danger")
        return redirect(url_for('locations.getAll'))