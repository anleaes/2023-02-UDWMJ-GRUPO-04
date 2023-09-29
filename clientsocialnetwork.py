from socialnetwork import Socialnetwork
from client import Client

class Clientsocialnetwork:
    
    def __init__(self,name, description, first_name, last_name, address, cell_phone, email, gender):
        self.name = name
        self.description = description
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.cell_phone = cell_phone
        self.mail = email
        self.gender = gender