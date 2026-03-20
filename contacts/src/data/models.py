from dataclasses import dataclass


@dataclass
class contactos:
    name :str
    number :str


    def __str__(self):
        return f"""---
name: {self.name}
number: {self.number}
---
# Contact
"""
    
@dataclass
class ContactInfo:
    contact: contactos
    path: str