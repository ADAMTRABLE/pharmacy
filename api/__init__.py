from flask import Flask,app
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict

from .utils import db
from .models.orders import Order
from  .models.users import User

from flask_migrate import Migrate

def create_app(config=config_dict['dev']):
    app=Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate= Migrate(db,app)

    api = Api(app)

    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace)

    @app.shell_context_processor
    def make_shell_context():
        return { 
            'db': db,
            'Order': Order,
            'User': User
        }

    return app


if __name__ == "__main__":
    app.run(debug=True)