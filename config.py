import os

class Config:

    SECRET_KEY = '2004'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://steve:steve1234@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    QUOTE_API_BASE_URL = "http://quotes.stormconsultancy.co.uk/random.json" 

    UPLOADED_PHOTOS_DEST ='app/static/photos'
 
    
  

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE = os.environ.get("DATABASE_URL")
    pass 

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://steve:steve1234@localhost/blog' 
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}