import os


class Config(object):
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        db_url = os.environ.get("DATABASE_URL")

        if not db_url:
            raise ValueError("Database URL is not set")
        return db_url
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass


app_environment = os.environ.get("FLASK_DEBUG")

if app_environment:
    app_config = DevelopmentConfig()
else:
    app_config = ProductionConfig()