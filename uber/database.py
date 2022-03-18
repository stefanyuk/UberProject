from flask.cli import with_appcontext
import click
from uber import db


def reset_db():
    db.drop_all()
    db.create_all()


@click.command('reset-db')
@with_appcontext
def reset_db_command():
    """Clear the existing data and create new tables."""
    reset_db()
    click.echo('Database has been reset.')
