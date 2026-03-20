from data.models import contactos
from services import database

def create(name: str, number: str):
    if not name.replace(" ", "").isalpha():
        print(f"Erro: '{name}' isn´t a valid name. Use only letters.")
        return

    if not str(number).isdigit():
        print(f"Erro: '{number}' isn´t a valid number. Use only numeric values.")
        return

    new_contact = contactos(
        name=name,
        number=number
    )
    
    database.create(contact=new_contact)
    print(f"Contact {name} created successfully!")