from app.extensions import db
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

    

    def __init__ (self, name,description, price):
          super(Product, self).__init__()
                         
          self.name = name   
          self.description = description           
          self.price= price
          
         
        

    def product_info(self):
       return  f" {self.name} {self.description}"