
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import user
from models.role import role
from data.db import db

users = Blueprint('users', __name__)

@users.route("/user", methods=["GET"])
def getAll():
    # usr = user.query.all()
    userfilter = user.query.all()
    return render_template('user/list.html',userfilter = userfilter)

    # return render_template('role/list.html',roles=roles)

@users.route("/user/<id>", methods=["GET"])
def getbyid(id):
    return "Role by id"

@users.route("/user/create", methods=["POST", "GET"])
def create():
    roles = role.query.all()
    if request.method == 'GET':
        return render_template('user/create.html',roles=roles)
    
    roleId = request.form['roleId']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    address = request.form['address']
    phone = request.form['phone']
    docNumber = request.form['docNumber']
    mail = request.form['mail']
    userName = request.form['userName']
    userPass = request.form['userPass']

    if roleId == '':
        flash("Debe seleccionar el permiso","alert alert-danger")
        return render_template('user/create.html',roles=roles)
    if firstName == '':
        flash("Debe ingresar el nombre","alert alert-danger")
        return render_template('user/create.html',roles=roles)
    if lastName == '':
        flash("Debe ingresar el apellido","alert alert-danger")
        return render_template('user/create.html',roles=roles)
    if address == '':
        flash("Debe ingresar la direccion","alert alert-danger")
        return render_template('user/create.html',roles=roles)
    if phone == '':
        flash("Debe ingresar el telefono","alert alert-danger")
        return render_template('user/create.html',roles=roles)
    if docNumber == '':
        flash("Debe ingresar el numero de documento","alert alert-danger")
        return render_template('user/create.html',roles=roles)
    if mail == '':
        flash("Debe ingresar el correo electronico","alert alert-danger")
        return render_template('user/create.html',roles=roles)
    if userName == '':
        flash("Debe ingresar el nombre de usuario","alert alert-danger")
        return render_template('user/create.html',roles=roles) 
    if userPass == '':
        flash("Debe ingresar la contraseña del usuario","alert alert-danger")
        return render_template('user/create.html',roles=roles)      

    new_user = user(roleId,firstName,lastName,address,phone,docNumber,mail,userName,userPass,1)

    db.session.add(new_user)
    db.session.commit()

    flash("El usuario se guardo correctamente", "alert alert-success")

    return redirect(url_for('users.getAll'))

@users.route("/user/update/<id>", methods=["POST", "GET"])
def update(id):
    if request.method == 'POST':
        upd = user.query.get(id)

        firstName = request.form['firstName']
        lastName = request.form['lastName']
        address = request.form['address']
        phone = request.form['phone']
        docNumber = request.form['docNumber']
        mail = request.form['mail']

        if firstName == '':
            flash("Debe ingresar el nombre","alert alert-danger")
            return redirect(url_for('user.create'))
        if lastName == '':
            flash("Debe ingresar el apellido","alert alert-danger")
            return redirect(url_for('user.create'))
        if address == '':
            flash("Debe ingresar la direccion","alert alert-danger")
            return redirect(url_for('user.create'))
        if phone == '':
            flash("Debe ingresar el telefono","alert alert-danger")
            return redirect(url_for('user.create'))
        if docNumber == '':
            flash("Debe ingresar el numero de documento","alert alert-danger")
            return redirect(url_for('user.create'))
        if mail == '':
            flash("Debe ingresar el correo electronico","alert alert-danger")
            return redirect(url_for('user.create')) 

        upd.firstName = firstName
        upd.lastName = lastName
        upd.address = address
        upd.phone = phone
        upd.docNumber = docNumber
        upd.mail = mail
        
        db.session.commit()

        flash("El usuario se actualizo correctamente", "alert alert-success")

        return redirect(url_for('users.getAll'))
    else:    
        updaterol = user.query.get(id)
        return render_template('update.html', updates=updaterol)

@users.route("/user/delete/<id>")
def delete(id):
    dele = user.query.get(id)
    if dele is None:
        flash("Debe ingresar el correo electronico","alert alert-danger")

    dele.state = 2    
    db.session.commit()
    
    flash("El permiso se elimino correctamente", "alert alert-success")

    return redirect(url_for('users.getAll'))