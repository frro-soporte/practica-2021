from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import contact 
from data.db import db
from flask_login import current_user, login_required
from datetime import datetime

contacts = Blueprint('contacts', __name__)

@contacts.route("/contacts", methods=["GET"])
@login_required
def getAll():
    cont = contact.query.all()
    return render_template('contact/list.html',cont = cont)


@contacts.route("/contact/create", methods=["POST", "GET"])
@login_required
def create():
    if request.method == 'GET':
        return render_template('contact/create.html')
    
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    description = request.form['description']
    createDate = datetime.now()
    finalDate = None
    state = 1

    if name == '':
        flash("Debe ingresar la ubicación.","alert alert-danger")
        return redirect(url_for('locations.create'))
    
    if email == '':
        flash("Debe ingresar el email.","alert alert-danger")
        return redirect(url_for('locations.create'))
    
    

    add = contact(fullname=name, email=email, phone=phone, description=description,createDate = createDate,finalDate=finalDate, state=state)
    db.session.add(add)
    db.session.commit()

    flash("El contacto se guardo correctamente", "alert alert-success")

    return redirect(url_for('contacts.getAll'))

@contacts.route("/contact/update/<id>", methods=["POST", "GET"])
@login_required
def update(id):
    if request.method == 'POST':
        c = contact.query.get(id)
        
        c.fullname = request.form['name']
        c.finalDate = request.form['finaldate']
        c.phone = request.form['phone']
        c.description = request.form['description']
        c.state = request.form['state']
        
        db.session.commit()

        flash("El contacto se actualizo correctamente", "alert alert-success")

        return redirect(url_for('contacts.getAll'))
    else:    
        updateid = contact.query.get(id)
        return render_template('contact/update.html', contacto=updateid)

@contacts.route("/contact/delete/<id>")
@login_required
def delete(id):
   try:
        dele = contact.query.get(id)
        db.session.delete(dele)
        db.session.commit()
        
        flash("El contacto se eliminó correctamente", "alert alert-success")

        return redirect(url_for('contacts.getAll'))
   except Exception as ex:
        flash("No se puede eliminar este contacto","alert alert-danger")
        return redirect(url_for('cpntacts.getAll'))