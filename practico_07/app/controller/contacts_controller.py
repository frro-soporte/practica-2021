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
from ..helpers import helper
from ..models.models import Contact


def create(contact_: Contact) -> Contact:
    contact_new = contact_db.create(contact_)
    return contact_new


def update(contact_: Contact) -> Contact:
    contact_new = contact_db.update(contact_)
    return contact_new


def delete(contact: Contact) -> Contact:
    contact_new = contact_db.delete(contact.id)
    return contact_new


def lists() -> List[Contact]:
    contacts = contact_db.list_all()
    return contacts


def details(contact: Contact) -> Contact:
    contact_new = contact_db.detail(contact)
    return contact_new
