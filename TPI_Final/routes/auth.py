from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user,login_required

from models.user import user
from models.auth import Auth
from data.db import db
import data
import json

auths = Blueprint('auth', __name__)

@auths.route("/", methods=["GET"])
def login():
    return redirect('auth')
    # return render_template('auth/login.html')

@auths.route("/auth", methods=["POST", "GET"])
def auth():
    try:
        if request.method == 'GET':
            return render_template('auth/login.html')  
    
        usrName = request.form['userName']
        userPass = request.form['userPass']
        if usrName == '':
            flash("Debe ingresar el nombre de usuario","alert alert-danger")
            return redirect(url_for('auth.login')) 
        if userPass == '':
            flash("Debe ingresar la contraseña del usuario","alert alert-danger")
            return redirect(url_for('auth.login')) 
        
        result = user.query.filter_by(userName=usrName).first()
        print("login result: ",result.id)
        if result:
            authentication = Auth(result.id,result.roleId,result.firstName,result.lastName,result.address,result.phone,result.docNumber,result.mail,result.userName,Auth.check_password(result.userPass,userPass))
            if authentication.userPass:
                print("authentication login: ",authentication)
                login_user(authentication)
                print("login_user login: ",authentication)
                return redirect(url_for('auth.home'))
            else:
                flash("Usuario y/o contraseña son incorrecto","alert alert-danger")
                return render_template('auth/login.html') 
        else:
            flash("Usuario y/o contraseña son incorrecto","alert alert-danger")
            return render_template('auth/login.html') 
        
    except Exception as ex:
        flash("error login","alert alert-danger")
        return redirect(url_for('auth.login')) 
    
@auths.route("/home", methods=["GET"])   
@login_required
def home():
    datos_diccionario = json.loads(datos_JSON)
    print("datos_diccionario ",datos_diccionario);
    return render_template('layout.html',products = datos_diccionario)

@auths.route("/logout", methods=["GET"])   
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
 
def status_401(error):
    return redirect(url_for('auth.login'))
def status_404(error):
    return "<h1>Pagina no encontrada</h1>", 404

datos_JSON =  """
[ {
      "name": "Quimica",
      "url": "kayak1.jpg"
    },
    {
        "name": "Administracion de recurso",
        "url": "kayak2.jpg"
    },
    {
        "name": "Economia",
        "url": "kayak3.jpg"
    },
    {
        "name": "ESTRUCTURA DE DATOS",
        "url": "kayak4.jpg"
    },
    {
        "name": "Legislation",
        "url": "CARPAS_PAGINA_WEB.jpg"
    }
]
"""