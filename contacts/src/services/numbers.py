from data.models import contactos
from services import database

def create(name: str, number: float):
    new_contact = contactos(
        name = name,
        number = number
    )
    database.create(contact = new_contact)

