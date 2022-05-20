import os
class Config:   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    QUOTE_KEY = 'http://quotes.stormconsultancy.co.uk/random.json'
    
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL",)
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://",1)
    # pass
    
class TestConfig(Config):
    
    pass

class DevConfig(Config):
 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eshi:1234@localhost/blogs'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}