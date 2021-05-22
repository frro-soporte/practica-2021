from flask import Blueprint, render_template, request, jsonify

from ..controller import contacts_controller
from ..models.models import Contact

nav = [
    {"name": "Example url 1", "url": "https://example.com/1"},
    {"name": "Example url 2", "url": "https://example.com/2"},
    {"name": "Example url 3", "url": "https://example.com/3"},
    {"name": "New Contact", "url": "/contacts/new-contact"},
]

global_scope = Blueprint("views", __name__)

@global_scope.route("/", methods=['GET'])
def home():
    """Landing page route."""

    parameters = { "title": "Flask and Jinja Practical work",
                    "description": "This is a simple page made for implement the basics concepts of Flask and Jinja2"
                 }

    return render_template("home.html", nav=nav, **parameters)


@global_scope.get("/contacts/new-contact'")
def form_post():
    title = "Flask and Jinja Practical work"
    description = "this is a simple page made for implement the basics concepts of Flask and Jinja2"

    return render_template("form.html", nav=nav, title=title, description=description)

