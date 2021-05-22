from flask import render_template, request, jsonify

from . import app
from .controller import contacts_controller
from .models.models import Contact

nav = [
    {"name": "Example url 1", "url": "https://example.com/1"},
    {"name": "Example url 2", "url": "https://example.com/2"},
    {"name": "Example url 3", "url": "https://example.com/3"},
    {"name": "New Contact", "url": "/contacts/new-contact"},
]


@app.route("/", methods=['GET'])
def home():
    """Landing page route."""

    parameters = { "title": "Flask and Jinja Practical work",
                    "description": "This is a simple page made for implement the basics concepts of Flask and Jinja2"
                 }

    return render_template("home.html", nav=nav, **parameters)


@app.get("/contacts/new-contact'")
def form_post():
    title = "Flask and Jinja Practical work"
    description = "this is a simple page made for implement the basics concepts of Flask and Jinja2"

    return render_template("form.html", nav=nav, title=title, description=description)


@app.route('/contacts', methods=['GET'])
def get_list():
    contacts_list = contacts_controller.lists()

    contacts_dict = [contact._asdict() for contact in contacts_list]

    return jsonify(contacts_dict)


@app.route('/contacts/<id_>', methods=['GET'])
def get_details(id_):
    contact = Contact(id=id_)

    contact_new = contacts_controller.details(contact)

    return jsonify(contact_new._asdict())


@app.route('/contacts', methods=['POST'])
def create():
    data = request.json
    contact = Contact(first_name=data["firstName"], last_name=data["lastName"], 
                      address=data["address"], city=data["city"], state=data["state"], 
                      zip_code=data["zipCode"], phone=data["phone"], email=data["email"])

    contact_new = contacts_controller.create(contact)

    return jsonify(contact_new._asdict())


@app.route('/contacts/<id_>', methods=['PUT'])
def update(id_):
    data = request.data

    contact = Contact(id=id_, first_name=data["firstName"], last_name=data["lastName"], 
                      address=data["address"], city=data["city"], state=data["state"], 
                      zip_code=data["zipCode"], phone=data["phone"], email=data["email"])

    contact_new = contacts_controller.update(contact)
        
    return jsonify(contact_new._asdict())


@app.route('/contacts/<id_>', methods=['DELETE'])
def delete(id_):
    contact = Contact(id=id_)

    contact_new = contacts_controller.delete(contact)

    return jsonify(contact_new._asdict())
