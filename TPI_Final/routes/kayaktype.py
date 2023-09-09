from flask import Blueprint, render_template, request, redirect, url_for, flash,jsonify, abort
from models.kayaktype import kayaktype
from flask.views import MethodView
from data.db import db
from flask_login import current_user, login_required

import uuid
import os

from io import BytesIO
from PIL import Image
import base64


kayaktypes = Blueprint('kayaktypes', __name__)

@kayaktypes.route("/kayaktypes", methods=["GET"])
@login_required
def getAll():
    loc = kayaktype.query.all()
    return render_template('kayaks/kayaktype/list.html',locs=loc)

@kayaktypes.route("/kayaktypes/<id>", methods=["GET"])
def getbyid(id):
    return kayaktype.query.get(id)
@kayaktypes.route("/kayaktypes/Upload", methods=["GET"])
def Upload():
            image_data = request.json['data']
            extension = request.json['extension']

            image_data = bytes(image_data, encoding="ascii")

            image_name = str(uuid.uuid4()) + extension

            image = Image.open(BytesIO(base64.b64decode(image_data)))
            image_directory = os.path.join(os.getcwd(), 'static', 'upload', 'image','')

            file_path = image_directory + image_name
            
            # save image to file system
            image.save(file_path)

            response = {
                "message": "Image Uploaded",
                "body": {
                    "image_id": image_name,
                }
            }
            return jsonify(response)

@kayaktypes.route("/kayaktypes/create", methods=["POST", "GET"])
def create():
    if request.method == 'GET':
        return render_template('kayaks/kayaktype/create.html')
    
    name = request.form['name']
    userId = current_user.id
    description = request.form['description']
    
    isexist = kayaktype.query.filter_by(name=name).first()
    if isexist :
        flash("Ya existe un tipo de kayak con ese nombre","alert alert-danger")
        return redirect(url_for('kayaktypes.create'))

    if name == '':
        flash("Debe ingresar el tipo de kayak.","alert alert-danger")
        return redirect(url_for('kayaktypes.create'))
    if len(name) > 251:
        flash("La cantidad de caracteres en el nombre no puede ser mayor que 100.","alert alert-danger")
    if len(description) > 251:
        flash("La cantidad de caracteres en la descripcion no puede ser mayor que 250.","alert alert-danger")
        return redirect(url_for('kayaktypes.create'))

    add = kayaktype(userId,name,description,1)

    db.session.add(add)
    db.session.commit()

    flash("El tipo de kayak se guardo correctamente", "alert alert-success")

    return redirect(url_for('kayaktypes.getAll'))

@kayaktypes.route("/kayaktypes/update/<id>", methods=["POST", "GET"])
def update(id):
    if request.method == 'POST':
        update = kayaktype.query.get(id)
        
        update.name = request.form['name']
        update.description = request.form['description']
        
        db.session.commit()

        flash("El tipo de kayak  se actualizo correctamente", "alert alert-success")

        return redirect(url_for('kayaktypes.getAll'))
    else:    
        updateid = kayaktype.query.get(id)
        return render_template('kayaks/kayaktype/update.html', updates=updateid)

@kayaktypes.route("/kayaktypes/delete/<id>")
def delete(id):
   try:
        dele = kayaktype.query.get(id)
        db.session.delete(dele)
        db.session.commit()
        
        flash("kayaktypes se elimino correctamente", "alert alert-success")

        return redirect(url_for('kayaktypes.getAll'))
   except Exception as ex:
        flash("No se puede eliminar este tipo de kayak porque tiene kayak asociado","alert alert-danger")
        return redirect(url_for('kayaktypes.getAll'))