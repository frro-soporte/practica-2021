"""
    
### Modelo Socios

 Es la representación de la información con la cual el sistema opera,\n
 por lo tanto gestiona todos los accesos a dicha información,\n
 tanto consultas como actualizaciones, implementando también los privilegios\n
 de acceso que se hayan descrito en las especificaciones de la aplicación (lógica de negocio).\n

    Restricciones ::

    
    1 : 'independiente de la vista y el controlador, estos dos dependen del modelo.'


"""

from DB import config
import sqlite3


def create(data):
    print(data)
    try:
        if check_user("email", data["email"]):
            return False, "Email already exists!", 400
        else:
            connect, cursor = config.db_connection()
            insert_id = insert_data(cursor, data)
            config.db_connection_close(connect)

            return insert_id, "", 200
    except sqlite3.Error as e:
        return e.args[0], 400


def insert_data(cursor, data):
    cursor.execute("INSERT INTO contacts VALUES ("
                   ":first_name, :last_name, :address, :city, :state, "
                   ":zip_code, :phone, :email)", {
                       'first_name': data["firstName"],
                       'last_name': data["lastName"],
                       'address': data["address"],
                       'city': data["city"],
                       'state': data["state"],
                       'zip_code': data["zipCode"],
                       'phone': data["phone"],
                       'email': data["email"],
                   })
    return cursor.lastrowid


def update(id, data):
    try:
        if check_user("oid", id):
            connect, cursor = config.db_connection()
            updated_id = update_data(cursor, id, data)
            config.db_connection_close(connect)

            return updated_id, "", 200
        else:
            return False, "Contact not Found!", 404
    except sqlite3.Error as e:
        return e.args[0], 400


def update_data(cursor, id, data):
    cursor.execute("""UPDATE contacts SET
                           first_name = :first_name,
                           last_name = :last_name,
                           address = :address,
                           city = :city,
                           state = :state,
                           zip_code = :zip_code,
                           phone = :phone,
                           email = :email
                           WHERE oid = :oid""",
                   {
                       'first_name': data["firstName"],
                       'last_name': data["lastName"],
                       'address': data["address"],
                       'city': data["city"],
                       'state': data["state"],
                       'zip_code': data["zipCode"],
                       'phone': data["phone"],
                       'email': data["email"],
                       'oid': id
                   })
    return id


def delete(id):
    try:
        if check_user("oid", id):
            connect, cursor = config.db_connection()
            deleted_id = delete_data(cursor, id)
            config.db_connection_close(connect)

            return deleted_id, "", 200
        else:
            return False, "Contact not Found!", 404
    except sqlite3.Error as e:
        return e.args[0], 400


def delete_data(cursor, id):
    cursor.execute("""DELETE FROM contacts WHERE oid = :oid""",
                   {
                       'oid': id
                   })
    return id


def list():
    try:
        connect, cursor = config.db_connection()
        cursor.execute("SELECT oid, * FROM contacts")
        records = cursor.fetchall()
        config.db_connection_close(connect)

        return records, 200
    except sqlite3.Error as e:
        return e.args[0], 400


def detail(id):
    try:
        connect, cursor = config.db_connection()
        cursor.execute(f"SELECT oid, * FROM contacts WHERE oid={id}")
        records = cursor.fetchall()
        config.db_connection_close(connect)

        return records, 200
    except sqlite3.Error as e:
        return e.args[0], 400


def check_user(field, value):
    connect, cursor = config.db_connection()
    cursor.execute(f"SELECT oid, email FROM contacts WHERE {field}='{value}'")
    record = cursor.fetchone()
    config.db_connection_close(connect)
    print(record)

    if record:
        return True
    else:
        return False
