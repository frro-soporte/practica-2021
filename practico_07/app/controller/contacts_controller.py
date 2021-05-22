"""
    
### Controlador Socios

Responde a eventos (usualmente acciones del usuario) e invoca peticiones al ‘modelo’ \n
cuando se hace alguna solicitud sobre la información (por ejemplo, editar un documento o un \n
registro en una base de datos). También puede enviar comandos a su ‘vista’ asociada si se solicita\n
un cambio en la forma en que se presenta el ‘modelo’, por tanto se podría decir que el ‘controlador’\n
hace de intermediario entre la ‘vista’ y el ‘modelo’.

    Restricciones ::

    
    1 : 'El controlador no debe realizar llamadas a la base de datos ni participar en la visualización de datos.'

"""

from typing import List

from ..database import contact_db
from ..models.models import Contact
from ..helpers import helper


def create(contact_: Contact) -> Contact:
    contact = helper.format_name(contact_)
    helper.validate_contact(contact)
    return contact_db.create(contact)


def update(contact: Contact) -> Contact:
    contact = helper.format_name(contact)
    helper.validate_contact(contact)
    return contact_db.update(contact)


def delete(contact: Contact) -> Contact:
    return contact_db.delete(contact.id)


def lists() -> List[Contact]:
    return contact_db.list_all()


def details(contact: Contact) -> Contact:
    return contact_db.detail(contact)
