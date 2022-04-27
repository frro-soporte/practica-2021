"""
### HELPERS

  Un Helper se compone de funciones genéricas que
  se encargan  de realizar acciones complementarias,
  aplicables a cualquier elemento de un sistema.
"""
import re

from ..models.models import Contact
from ..models.exceptions import UserNotValid


def validate_contact(contact: Contact) -> None:
    if not __email_is_valid(contact.email):
        raise UserNotValid(f"The email address: {contact.email} is not valid")

    if None in (contact.first_name, contact.last_name, contact.email):
        raise UserNotValid("The user has no first name, last name or email")


def format_name(contact: Contact) -> Contact:
    contact_dict = contact._asdict()
    contact_dict["first_name"] = contact.first_name.capitalize()
    contact_dict["last_name"] = contact.first_name.capitalize()

    return Contact(**contact_dict)


def __email_is_valid(email: str) -> bool:
    if not isinstance(email, str):
        return False

    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    return bool(re.search(regex, email))
