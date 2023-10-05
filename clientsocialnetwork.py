class Clientsocialnetwork:
    
    def __init__(self, client, socialnetwork):
        self.client = client
        self.socialnetwork = socialnetwork 

    def check_status(self):
        print(f"Cliente: {self.first_name} {self.last_name}/ Gênero:{self.gender}/ Endereço:{self.address}/ Telefone:{self.cell_phone}/ Email:{self.email}.")
