"""
### HELPERS

  Un Helper se compone de funciones genéricas que  \n    
  se encargan  de realizar acciones complementarias,  \n 
  aplicables a cualquier elemento de un sistema.  \n     


"""

from flask import jsonify


def response(data, message, status):
    """
    Funcion de uso comun para formatear 
    las respuestas que se envian a los usuarios

    - tags:
      - Formateador 

    parameters:

    - param1
        - name: data
        - type: string
    - param2
        - name: message
        - type: string
    - param3
        - name: status
        - type: integer
        - description: httpStatus


    Returns:
        Dict :  Diccionario(JSON) con formato estandar 
    """

    res = {
        "data": data,
        "message": message,
        "status": status
    }

    return jsonify(res)
