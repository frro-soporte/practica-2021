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


from models import Contact
from helpers import helper


def create(request_data):

    insert_id, message, status = Contact.create(request_data)

    if status != 200:
        return helper.response({"title": message}, "fail", status)
    else:
        return helper.response({"id": insert_id}, "success", status)


def update(request_data, contact_id):
    updated_id, message, status = Contact.update(contact_id, request_data)

    if status != 200:
        return helper.response({"title": message}, "fail", status)
    else:
        return helper.response({"id": updated_id}, "success", status)


def delete(contact_id):
    deleted_id, message, status = Contact.delete(id)

    if status != 200:
        return helper.response({"title": message}, "fail", status)
    else:
        return helper.response({"id": deleted_id}, "success", status)


def lists():
    records, status = Contact.list()

    if status != 200:
        return helper.response({}, records, status)
    else:
        results = []
        for record in records:
            data = {
                "id": record[0],
                "firstName": record[1],
                "lastName": record[2],
                "email": record[8]
            }
            results.append(data)

        return helper.response(results, "success", status)


def details(contact_id):
    records, status = Contact.detail(contact_id)

    if status != 200:
        return helper.response({}, records, status)
    else:
        results = []
        for record in records:
            data = {
                "id": record[0],
                "firstName": record[1],
                "lastName": record[2],
                "address": record[3],
                "city": record[4],
                "state": record[5],
                "zipCode": record[6],
                "phone": record[7],
                "email": record[8]
            }
            results.append(data)

        return helper.response(results, "message", "success")
