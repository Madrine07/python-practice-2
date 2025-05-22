from datetime import timedelta

class Config:
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/product_db'
     JWT_SECRET_KEY = "exam" 
     JWT_EXPIRATION_DELTA = timedelta(minutes=10)
     DEBUG = True
