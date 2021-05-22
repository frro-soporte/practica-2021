"""
    
### Modelo Socios

 Es la representación de la información con la cual el sistema opera,\n
 por lo tanto gestiona todos los accesos a dicha información,\n
 tanto consultas como actualizaciones, implementando también los privilegios\n
 de acceso que se hayan descrito en las especificaciones de la aplicación (lógica de negocio).\n

    Restricciones ::

    
    1 : 'independiente de la vista y el controlador, estos dos dependen del modelo.'


"""

from typing import List

from .connection import _fetch_all, _fetch_lastrow_id, _fetch_none, _fetch_one
from ..models.models import Contact
from ..models.exceptions import UserAlreadyExists, UserNotFound


def create(contact: Contact) -> Contact:
    if user_exists("email", contact.email):
        raise UserAlreadyExists(f"Email {contact.email} is already used")

    query = """INSERT INTO contacts VALUES (:first_name, :last_name, 
                                            :address, :city, :state, 
                                            :zip_code, :phone, :email)"""

    contact_dict = contact._asdict()

    id_ = _fetch_lastrow_id(query, contact_dict)

    contact_dict["id"] = id_
    return Contact(**contact_dict)


def update(contact: Contact) -> Contact:
    if not user_exists("oid", contact.id):
        raise UserNotFound("Contact not Found!")

    query = """UPDATE contacts SET first_name = :first_name, last_name = :last_name,
                      address = :address, city = :city, state = :state,
                      zip_code = :zip_code, phone = :phone, email = :email
               WHERE oid = :oid"""

    parameters = contact._asdict()

    _fetch_none(query, parameters)
    
    return contact


def delete(contact: Contact) -> Contact:
    if not user_exists("oid", contact.id):
        raise UserNotFound("Contact not Found!")

    query = "DELETE FROM contacts WHERE oid = ?"
    parameters = [contact.id]

    _fetch_none(query, parameters)

    return contact


def list_all() -> List[Contact]:
    query = "SELECT oid, * FROM contacts"
    records = _fetch_all(query)

    contacts = []
    for record in records:
        contact = Contact(id=record[0], first_name=record[1], last_name=record[2], 
                          address=record[3], city=record[4], state=record[5], 
                          zip_code=record[6], phone=record[7], email=record[8])
        contacts.append(contact)

    return contacts


def detail(contact: Contact) -> Contact:
    query = "SELECT oid, * FROM contacts WHERE oid=?"
    parameters = [contact.id]

    record = _fetch_one(query, parameters)

    if record is None:
        raise UserNotFound(f"No user with id: {contact.id}")
    
    contact = Contact(id=record[0], first_name=record[1], last_name=record[2], 
                      address=record[3], city=record[4], state=record[5], 
                      zip_code=record[6], phone=record[7], email=record[8])

    return contact


def user_exists(field: str, value: str) -> bool:
    query = f"SELECT oid, email FROM contacts WHERE {field}=?"
    parameters = [value]

    record = _fetch_one(query, parameters)

    return bool(record)
