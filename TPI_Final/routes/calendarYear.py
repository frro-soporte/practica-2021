from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.calendarYear import calendarYear 
from data.db import db
from flask_login import current_user, login_required
from datetime import datetime

calendarYears = Blueprint('calendarYears', __name__)

@calendarYears.route("/calendarYear", methods=["GET"])
@login_required
def getAll():
    cal = calendarYear.query.all()
    return render_template('calendarYear/list.html',cal = cal)

@calendarYears.route('/calendarYear/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('calendarYear/create.html')
    
    if request.method == 'POST':
        yearCalendar = request.form['yearCalendar']
        description = request.form['description']
        createDate = datetime.now()
        userId = current_user.id
        finalDate = None
        state = 1


        if yearCalendar == '':
            flash("Debe ingresar el número de año","alert alert-danger")
            return redirect(url_for('calendarYears.create'))
        
        add = calendarYear(userId=userId, yearCalendar=yearCalendar ,description=description,createDate=createDate, finalDate=finalDate, state=state)
        db.session.add(add)
        db.session.commit()

        flash("El calendario se guardo correctamente", "alert alert-success")

        return redirect(url_for('calendarYears.getAll'))
    


@calendarYears.route('/calendarYear/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    if request.method == 'POST':
        update = calendarYear.query.get(id)
        
        update.yearCalendar = request.form['year']
        update.description = request.form['description']
        
        db.session.commit()

        flash("El calendario se actualizo correctamente", "alert alert-success")

        return redirect(url_for('calendarYears.getAll'))
    else:    
        updateid = calendarYear.query.get(id)
        return render_template('calendarYear/update.html', c=updateid)
    

@calendarYears.route("/calendarYear/delete/<id>")
def delete(id):
   try:
        dele = calendarYear.query.get(id)
        db.session.delete(dele)
        db.session.commit()
        
        flash("El calendario se elimino correctamente", "alert alert-success")

        return redirect(url_for('calendarYears.getAll'))
   except Exception as ex:
        flash("No se puede eliminar esta ubicación porque tiene una entidad asociada","alert alert-danger")
        return redirect(url_for('calendarYears.getAll'))