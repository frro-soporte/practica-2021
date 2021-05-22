from flask import Blueprint, request, jsonify, redirect, url_for

from ..controller import contacts_controller
from ..models.models import Contact


api_scope = Blueprint("api", __name__)


@api_scope.route('/contacts', methods=['GET'])
def get_list():
    contacts_list = contacts_controller.lists()

    contacts_dict = [contact._asdict() for contact in contacts_list]

    return jsonify(contacts_dict)


@api_scope.route('/contacts/<id_>', methods=['GET'])
def get_details(id_):
    contact = Contact(id=id_)

    contact_new = contacts_controller.details(contact)

    return jsonify(contact_new._asdict())


@api_scope.route('/contacts', methods=['POST'])
def create():
    data = request.form
    print(data)
    contact = Contact(first_name=data["firstName"], last_name=data["lastName"],
                      address=data["address"], city=data["city"], state=data["state"],
                      zip_code=data["zipCode"], phone=data["phone"], email=data["email"])

    contacts_controller.create(contact)

    return redirect(url_for('views.home'))


@api_scope.route('/contacts/<id_>', methods=['PUT'])
def update(id_):
    data = request.data

    contact = Contact(id=id_, first_name=data["firstName"], last_name=data["lastName"],
                      address=data["address"], city=data["city"], state=data["state"],
                      zip_code=data["zipCode"], phone=data["phone"], email=data["email"])

    contact_new = contacts_controller.update(contact)

    return jsonify(contact_new._asdict())


@api_scope.route('/contacts/<id_>', methods=['DELETE'])
def delete(id_):
    contact = Contact(id=id_)

    contact_new = contacts_controller.delete(contact)

    return jsonify(contact_new._asdict())
