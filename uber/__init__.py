from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, directory=app.config['MIGRATION_DIR'])

    # cli commands
    from uber.database import reset_db_command
    app.cli.add_command(reset_db_command)

    from uber.views.register_lead import home
    app.register_blueprint(home)

    return app
