from flask import jsonify, Blueprint

from ..models.exceptions import UserAlreadyExists, UserNotFound, UserNotValid

errors_scope = Blueprint("errors", __name__)

def __generate_error_response(error):
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }
    return jsonify(message)


@errors_scope.app_errorhandler(UserNotFound)
def handle_foo_exception(error: UserNotFound):
    response = __generate_error_response(error)
    response.status_code = 404
    return response


@errors_scope.app_errorhandler(UserNotValid)
@errors_scope.app_errorhandler(UserAlreadyExists)
def handle_foo_exception(error: Exception):
    response = __generate_error_response(error)
    response.status_code = 409
    return response


@errors_scope.app_errorhandler(404)
def handle_foo_exception(error):
    response = __generate_error_response(error)
    response.status_code = 404
    return response
