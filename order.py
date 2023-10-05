class order:

 def __init__(self ,total_price,status,client):
  self.total_prices = total_price
  self.status = status
  self.client = client


 def lista (self):
     print (f"preço total = {self.total_price}. ")
     print (f"status = {self.status}. ")
     print (f"cliente = {self.client}. ")