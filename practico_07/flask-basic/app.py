from os import error
from sqlite3.dbapi2 import Error
import flask
from flask import request
from controllers import contacts
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

nav = [
    {"name": "Example url 1", "url": "https://example.com/1"},
    {"name": "Example url 2", "url": "https://example.com/2"},
    {"name": "Example url 3", "url": "https://example.com/3"},
    {"name": "New Contact", "url": "/contacts/new-contact"},
]


@app.route("/", methods=['POST'])
def home():
    """Landing page route."""
    return render_template(
        "home.html",
        nav=nav,
        title="Flask and Jinja Practical work",
        description="this is a simple page made for implement the basics concepts of Flask and Jinja2",
    )


@app.get("/contacts/new-contact'")
def form_post():
    return render_template(
        "form.html",
        nav=nav,
        title="Flask and Jinja Practical work",
        description="this is a simple page made for implement the basics concepts of Flask and Jinja2",
    )


@app.route('/contacts', methods=['POST'])
def create():
    request_data = request.json
    return contacts.create(request_data)


@app.route('/contacts/<contact_id>', methods=['PUT'])
def update(contact_id):
    return contacts.update(contact_id)


@app.route('/contacts/<contact_id>', methods=['DELETE'])
def delete(contact_id):
    request_data = request.data
    return contacts.delete(request_data, contact_id)


@app.route('/contacts', methods=['GET'])
def get_list():
    return contacts.lists()


@app.route('/contacts/<contact_id>', methods=['GET'])
def get_details(contact_id):
    return contacts.details(contact_id)


app.run()
