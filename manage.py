import os
import unittest

from app import blueprint
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app.main import create_app, db

from app.main.model import user
from app.main.model import blacklist

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

cli = FlaskGroup(app)
migrate = Migrate(app, db)


@cli.command
def run():
    app.run()


@cli.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
