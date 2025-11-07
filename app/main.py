from flask import Flask
from flask_restx import Api
from db import init_db
from routes import api as store_api
from settings_config import *

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@db:{db_port}/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app, version=f"{app_version}", title=f"{app_title}", description=f"{app_description}")
    api.add_namespace(store_api, path="/api")

    init_db(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
