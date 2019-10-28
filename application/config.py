import os 


class Config:
    TESTING= False
    DEBUG=False

class DevConfig(Config):
    TESTING=True
    DEBUG=True
    SECRET_KEY='dev'
        
    # Database
    SQLALCHEMY_DATABASE_URI =  "sqlite:///NetotlabDev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):

    TESTING=True
    DEBUG=True
    SECRET_KEY='dev'
        
    # Database
    #SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI"),
    #SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
