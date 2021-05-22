from flask import jsonify

from .models.exceptions import UserAlreadyExists, UserNotFound
from . import app


@app.errorhandler(UserNotFound)
def handle_foo_exception(error: UserNotFound):
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }
    response = jsonify(message)
    response.status_code = 404
    return response


@app.errorhandler(UserAlreadyExists)
def handle_foo_exception(error: UserAlreadyExists):
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }
    response = jsonify(message)
    response.status_code = 409
    return response
